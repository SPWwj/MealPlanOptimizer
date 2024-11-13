# Meal Plan Optimizer

This program generates optimized meal plans based on user-defined constraints such as calorie range, budget, sodium, protein, carbohydrates, and fat. The goal is to minimize cost while meeting nutritional needs for specific meal types (breakfast, lunch, or dinner).

### Features
- **Flexible Nutritional Constraints**: Set minimum/maximum values for calories, protein, carbs, fat, and sodium.
- **Cost Minimization**: The program minimizes the cost of the meal plan while respecting dietary limits.
- **Meal Type Selection**: Choose meal type (breakfast, lunch, dinner) for targeted meal planning.
- **Unique or Multiple Selections**: Allows the option to select unique items or multiple servings.

### Requirements

To set up the environment, you need Python and the following packages:

```bash
pip install pulp
```

### Program Files

1. **menu_builder.py**: Main code that defines `get_best_meal()` and implements the optimization logic.
2. **test_meal_plan.py**: Test script containing various test cases to validate the meal plan generation under different constraints.

### Running the Test

To try out the program with sample test cases, run:

```bash
python test_meal_plan.py
```

This will output optimal meal plans or notify if constraints are too strict to generate a feasible plan.
