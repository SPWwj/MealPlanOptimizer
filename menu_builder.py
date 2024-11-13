import argparse
import json
from pulp import PULP_CBC_CMD, LpProblem, LpMinimize, LpVariable, lpSum, LpStatus
from singapore_food_data import create_singapore_food_database


def create_meal_plan_lp(food_items, min_calories, max_calories, max_sodium, max_budget, min_protein, max_carbs, max_fat, unique=True):
    # Changed to LpMinimize to minimize total cost
    prob = LpProblem("Meal_Plan_Optimization", LpMinimize)
    
    if unique:
        # Each food item can be selected at most once
        x = {item.name: LpVariable(f"x_{item.name}", cat="Binary") for item in food_items}
    else:
        # Food items can be selected multiple times
        x = {item.name: LpVariable(f"x_{item.name}", lowBound=0, cat="Integer") for item in food_items}
    
    locations = set(item.location for item in food_items)
    y = {loc: LpVariable(f"y_{loc}", cat="Binary") for loc in locations}

    # Objective function: Minimize total cost
    prob += lpSum(item.price * x[item.name] for item in food_items), "Total_Cost"

    # Nutritional constraints
    prob += lpSum(item.calories * x[item.name] for item in food_items) >= min_calories, "Min_Calories"
    prob += lpSum(item.calories * x[item.name] for item in food_items) <= max_calories, "Max_Calories"
    prob += lpSum(item.protein * x[item.name] for item in food_items) >= min_protein, "Min_Protein"
    prob += lpSum(item.carbs * x[item.name] for item in food_items) <= max_carbs, "Max_Carbs"
    prob += lpSum(item.fat * x[item.name] for item in food_items) <= max_fat, "Max_Fat"
    prob += lpSum(item.sodium * x[item.name] for item in food_items) <= max_sodium, "Max_Sodium"
    # Removed the budget constraint since we are minimizing cost
    # prob += lpSum(item.price * x[item.name] for item in food_items) <= max_budget, "Budget"
    # However, if you still want to enforce a maximum budget, uncomment the above line

    # Linking food items to locations
    for item in food_items:
        prob += x[item.name] <= y[item.location], f"Link_{item.name}_to_{item.location}"

    # Only one location can be selected
    prob += lpSum(y[loc] for loc in locations) == 1, "Single_Location"

    # Solve the problem
    prob.solve(PULP_CBC_CMD(msg=False))
    status = LpStatus[prob.status]

    # Check if the solution is optimal
    if status != 'Optimal':
        return [], status, 0

    selected_items = [(item, x[item.name].varValue) for item in food_items if x[item.name].varValue > 0]
    total_cost = sum(item.price * count for item, count in selected_items)
    return selected_items, status, total_cost


def generate_json_response(selected_items, status, total_cost):
    if status != 'Optimal':
        response = {
            "status": status,
            "message": "No feasible meal plan could be found with the given constraints."
        }
        return json.dumps(response, indent=4)

    response = {
        "status": status,
        "total_cost": total_cost,
        "meal_plan": [
            {
                "id": str(item.food_id),
                "name": item.name,
                "count": int(count),
                "location": item.location,
                "calories": item.calories,
                "protein": item.protein,
                "carbs": item.carbs,
                "fat": item.fat,
                "sodium": item.sodium,
                "price": item.price
            }
            for item, count in selected_items
        ]
    }
    return json.dumps(response, indent=4)


def get_best_meal(meal_type, constraints, unique=True):
    food_items = create_singapore_food_database()
    filtered_items = [item for item in food_items if meal_type in item.meal_type]
    selected_items, status, total_cost = create_meal_plan_lp(
        filtered_items,
        min_calories=constraints["min_calories"],
        max_calories=constraints["max_calories"],
        max_sodium=constraints["max_sodium"],
        max_budget=constraints["max_budget"],
        min_protein=constraints["min_protein"],
        max_carbs=constraints["max_carbs"],
        max_fat=constraints["max_fat"],
        unique=unique
    )
    return generate_json_response(selected_items, status, total_cost)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a meal plan based on constraints.")
    parser.add_argument("meal_type", type=str, help="Type of meal (e.g., breakfast, lunch, dinner)")
    parser.add_argument("--min_calories", type=int, default=0, help="Minimum calories required")
    parser.add_argument("--max_calories", type=int, default=1e6, help="Maximum calories allowed")
    parser.add_argument("--max_sodium", type=int, default=1e6, help="Maximum sodium allowed (mg)")
    parser.add_argument("--max_budget", type=float, default=1e6, help="Maximum budget allowed (SGD)")
    parser.add_argument("--min_protein", type=int, default=0, help="Minimum protein required (g)")
    parser.add_argument("--max_carbs", type=int, default=1e6, help="Maximum carbs allowed (g)")
    parser.add_argument("--max_fat", type=int, default=1e6, help="Maximum fat allowed (g)")
    
    # New unique parameter
    parser.add_argument('--unique', dest='unique', action='store_true', default=True, help="Ensure each food item is selected at most once (default)")
    parser.add_argument('--no-unique', dest='unique', action='store_false', help="Allow multiple servings of the same food item")
    
    args = parser.parse_args()
    constraints = {
        "min_calories": args.min_calories,
        "max_calories": args.max_calories,
        "max_sodium": args.max_sodium,
        "max_budget": args.max_budget,
        "min_protein": args.min_protein,
        "max_carbs": args.max_carbs,
        "max_fat": args.max_fat
    }

    response = get_best_meal(args.meal_type, constraints, unique=args.unique)
    print(response)
