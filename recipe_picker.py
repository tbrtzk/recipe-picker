from recipe import Recipe
import random


class RecipePicker:
    def __init__(self, recipe_list):
        self.recipe_bank = []
        self.filtered_recipes = []
        for recipe in recipe_list:
            name = recipe["name"]
            effort = recipe["effort"]
            health_level = recipe["health_level"]
            new_recipe = Recipe(name, effort, health_level)
            self.recipe_bank.append(new_recipe)

    def get_effort(self):
        return input("How complex should the recipe be?"
                     "Describe the effort with 'low', 'medium' or 'high'.\n".lower())

    def get_health_level(self):
        return input("How healthy do you want to eat today? Type 'super healthy', 'medium healthy' or 'comfort food'\n").lower()

    def filter_recipes(self):
        effort = self.get_effort()
        health_level = self.get_health_level()

        for recipe in self.recipe_bank:
            if recipe.effort == effort and recipe.health_level == health_level:
                self.filtered_recipes.append(recipe)

    def pick_recipe(self):
        self.filter_recipes()
        return random.choice(self.filtered_recipes).name





