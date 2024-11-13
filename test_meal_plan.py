from menu_builder import get_best_meal

def test_meal_plan():
    # Define multiple test cases with varying constraints
    test_cases = [
        {
            "description": "Low-calorie breakfast with budget constraint",
            "meal_type": "breakfast",
            "constraints": {
                "min_calories": 100,
                "max_calories": 300,
                "max_sodium": 500,
                "max_budget": 5.00,
                "min_protein": 5,
                "max_carbs": 50,
                "max_fat": 10
            },
            "unique": True
        },
        {
            "description": "High-protein lunch under moderate budget",
            "meal_type": "lunch",
            "constraints": {
                "min_calories": 500,
                "max_calories": 1000,
                "max_sodium": 800,
                "max_budget": 12.00,
                "min_protein": 25,
                "max_carbs": 100,
                "max_fat": 20
            },
            "unique": True
        },
        {
            "description": "Flexible dinner with multiple servings allowed",
            "meal_type": "dinner",
            "constraints": {
                "min_calories": 600,
                "max_calories": 1200,
                "max_sodium": 1200,
                "max_budget": 20.00,
                "min_protein": 30,
                "max_carbs": 80,
                "max_fat": 30
            },
            "unique": False
        },
        {
            "description": "Very strict low-fat dinner under tight budget",
            "meal_type": "dinner",
            "constraints": {
                "min_calories": 300,
                "max_calories": 500,
                "max_sodium": 300,
                "max_budget": 7.00,
                "min_protein": 15,
                "max_carbs": 60,
                "max_fat": 5
            },
            "unique": True
        },
        {
            "description": "High-calorie breakfast with high protein and low sodium",
            "meal_type": "breakfast",
            "constraints": {
                "min_calories": 400,
                "max_calories": 700,
                "max_sodium": 300,
                "max_budget": 10.00,
                "min_protein": 20,
                "max_carbs": 100,
                "max_fat": 20
            },
            "unique": True
        }
    ]
    
    # Run each test case
    for i, test_case in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: {test_case['description']}")
        response = get_best_meal(
            test_case["meal_type"],
            test_case["constraints"],
            unique=test_case["unique"]
        )
        print(response)

if __name__ == "__main__":
    test_meal_plan()
