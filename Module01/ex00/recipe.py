class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=""):
        self.name = name
        self.recipe_type = recipe_type
        self.description = description
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.cooking_lvl = cooking_lvl

    def __str__(self):
        """Returns the string to print with the recipe info"""
        txt = f"Receta: {self.name} \nTipo de receta: {self.recipe_type} \nIngredientes: {self.ingredients}\n{self.description}"

        return txt
