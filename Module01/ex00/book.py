class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        self.recipes_list = recipes_list
        self.creation_date = creation_date
        self.last_update = last_update
        self.name = name

    def get_recipe_by_name(self, name):
        """Print a recipe with the name \texttt{name} and returns the instance"""
        pass

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        pass

    def add_recipe(self, recipe):
        """Add a recipe to the book and update las_update"""
        pass
