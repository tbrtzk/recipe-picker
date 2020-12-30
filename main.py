from recipe_picker import RecipePicker
from data import recipes

recipe_picker = RecipePicker(recipes)
suggested_recipe = recipe_picker.pick_recipe()

print(f"Today you could cook {suggested_recipe}.")