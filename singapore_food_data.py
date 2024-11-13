class FoodItem:
    def __init__(self, food_id, name, calories, protein, carbs, fat, sodium, price, location, meal_type):
        self.food_id = food_id  # Static ID for each FoodItem
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.sodium = sodium
        self.price = price
        self.location = location
        self.meal_type = frozenset(meal_type)

    def __hash__(self):
        return hash(self.food_id)  # Hash based on static ID

    def __eq__(self, other):
        if isinstance(other, FoodItem):
            return self.food_id == other.food_id
        return False

def create_singapore_food_database():
    """
    Create and return Singapore food database using data from HealthHub.sg recipes

    DISCLAIMER: 
    - Nutritional data is sourced from HealthHub.sg recipes (https://www.healthhub.sg/programmes/parent-hub/recipes)
    - Restaurant locations are mock data for demonstration purposes only
    - Prices are estimated and for demonstration purposes only
    """
    # Updated locations
    CAFE_1 = "Cafe 1"
    FOOD_COURT = "Food Court"
    RESTAURANT_1 = "Restaurant 1"

    # Updated list of food items
    foods = [
        # Breakfast items
        FoodItem("B001", "Overnight Oats with Fruits", 286, 12, 45, 7, 124, 6.90, CAFE_1, {"breakfast"}),
        FoodItem("B002", "Greek Yogurt with Berries", 200, 12, 25, 5, 80, 5.50, CAFE_1, {"breakfast"}),
        FoodItem("B003", "Banana Nut Smoothie", 220, 10, 35, 5, 50, 4.20, CAFE_1, {"breakfast"}),
        FoodItem("B004", "Chinese-Style Carrot Cake with Chinese Sausage", 219, 6.2, 32.0, 7.3, 510, 4.50, CAFE_1, {"breakfast"}),
        FoodItem("B005", "Good Old Chapati and Dhal", 154.5, 7.1, 25.3, 2.2, 206.8, 3.40, CAFE_1, {"breakfast"}),
        FoodItem("B006", "Oriental Bee Hoon", 241, 10.3, 44.5, 2.5, 265.5, 4.30, CAFE_1, {"breakfast"}),
        FoodItem("B007", "Filet-O-Fish", 332, 15, 38, 13, 562, 4.75, CAFE_1, {"breakfast"}),
        FoodItem("B008", "Double Filet-O-Fish", 466, 24, 48, 20, 756, 6.8, CAFE_1, {"breakfast"}),
        FoodItem("B009", "Sausage McMuffin", 258, 16, 29, 9, 653, 3.8, CAFE_1, {"breakfast"}),
        FoodItem("B010", "Egg McMuffin", 289, 18, 29, 11, 574, 4.75, CAFE_1, {"breakfast"}),
        FoodItem("B011", "Scrambled Egg Burger with Sausage", 492, 30, 33, 26, 993, 5.2, CAFE_1, {"breakfast"}),
        FoodItem("B012", "Breakfast Wrap Chicken Ham", 430, 17, 43, 21, 1201, 5, CAFE_1, {"breakfast"}),

        # Lunch items
        FoodItem("L001", "Chicken Brown Rice Bowl", 409, 27, 62, 8, 378, 8.90, FOOD_COURT, {"lunch"}),
        FoodItem("L002", "Grilled Salmon with Quinoa", 750, 40, 70, 25, 400, 14.00, FOOD_COURT, {"lunch"}),
        FoodItem("L003", "Beef and Veggie Wrap", 720, 30, 65, 20, 500, 12.50, FOOD_COURT, {"lunch"}),
        FoodItem("L004", "Chicken Briyani", 190.8, 11.4, 35, 1.3, 234.7, 5.50, FOOD_COURT, {"lunch"}),
        FoodItem("L005", "Wantan Mee", 327.6, 16.9, 46.3, 7.6, 315.4, 6.50, FOOD_COURT, {"lunch"}),
        FoodItem("L006", "Fried Kway-Teow in Creamy Foo Yong Sauce", 302, 21.5, 34.5, 8.3, 643, 6.30, FOOD_COURT, {"lunch"}),
        FoodItem("L007", "Sliced Fish Bee Hoon Soup", 385, 21.1, 55.2, 8.8, 269.2, 5.80, FOOD_COURT, {"lunch"}),
        FoodItem("L008", "McSpicy", 541, 23, 50, 28, 1269, 6.8, FOOD_COURT, {"lunch"}),
        FoodItem("L009", "Double McSpicy", 833, 38, 66, 46, 2161, 7.95, FOOD_COURT, {"lunch"}),
        FoodItem("L010", "Buttermilk Crispy Chicken", 739, 26, 64, 42, 1422, 8.5, FOOD_COURT, {"lunch"}),
        FoodItem("L011", "Big Mac", 558, 28, 48, 28, 1321, 6.9, FOOD_COURT, {"lunch"}),
        FoodItem("L012", "Hamburger", 253, 14, 31, 8, 690, 2.95, FOOD_COURT, {"lunch"}),
        FoodItem("L013", "Double Cheeseburger", 443, 27, 34, 22, 1360, 5.3, FOOD_COURT, {"lunch"}),

        # Dinner items
        FoodItem("D001", "Lentil Soup with Whole Grain Bread", 400, 20, 55, 8, 250, 7.00, RESTAURANT_1, {"dinner"}),
        FoodItem("D002", "Grilled Chicken Salad", 320, 30, 12, 15, 290, 10.50, RESTAURANT_1, {"dinner"}),
        FoodItem("D003", "Baked Salmon with Sweet Potato", 650, 45, 45, 20, 500, 15.00, RESTAURANT_1, {"dinner"}),
        FoodItem("D004", "Spaghetti with Meatballs", 680, 35, 60, 18, 600, 12.00, RESTAURANT_1, {"dinner"}),
        FoodItem("D005", "Bamboo Pith And Tofu Parcels", 101, 11.5, 0.4, 7.3, 415, 13.00, RESTAURANT_1, {"dinner"}),
        FoodItem("D006", "Braised Mee Sua With Shredded Chicken", 244, 38.9, 0.9, 13.0, 373, 14.70, RESTAURANT_1, {"dinner"}),
        FoodItem("D007", "Traditional Teochew Steamed Fish", 171, 26.3, 7.1, 3.8, 559, 15.30, RESTAURANT_1, {"dinner"}),
        FoodItem("D008", "Grilled Chicken McWrap", 361, 23, 29, 18, 992, 6.6, RESTAURANT_1, {"dinner"}),
        FoodItem("D009", "Cheeseburger", 303, 16, 32, 12, 860, 3.65, RESTAURANT_1, {"dinner"}),
    ]
    
    return foods

# Test the updated database function
if __name__ == "__main__":
    for food in create_singapore_food_database():
        print(
            f"ID: {food.food_id}, "
            f"Name: {food.name}, "
            f"Calories: {food.calories}, "
            f"Protein: {food.protein}g, "
            f"Carbs: {food.carbs}g, "
            f"Fat: {food.fat}g, "
            f"Sodium: {food.sodium}mg, "
            f"Price: ${food.price:.2f}, "
            f"Location: {food.location}, "
            f"Meal Type: {', '.join(food.meal_type)}"
        )
