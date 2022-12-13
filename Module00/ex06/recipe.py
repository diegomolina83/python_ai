from prompt_toolkit import prompt

sandwich = {
    'ingredients': ["ham", "bread", "cheese", "tomatoes"],
    'meal': 'lunch',
    'prep_time': 10
}

cake = {
    'ingredients': ["flour", "sugar", "eggs"],
    'meal': 'dessert',
    'prep_time': 60
}
salad = {
    'ingredients': ["avocado", "arugula", "tomatoes", "spinach"],
    'meal': 'lunch',
    'prep_time': 15
}

cookbook = {
    "sandiwch": sandwich,
    "cake": cake,
    "salad": salad
}


def print_recipe_names():
    for keys in cookbook:
        print(keys)


def print_ingredients(ingredients):
    string = ""
    for ing in ingredients:
        string += f" {ing}"
    return string


def print_recipe_details(name):
    for keys, values in cookbook.items():
        if name == keys:
            print(f"The ingredients for this recipe are{print_ingredients(values.get('ingredients'))}")
            print(f"This recipe is the type {values.get('meal')}")
            print(f"We need {values.get('prep_time')} minutes to cook this recipe")


def delete_recipe(param):
    del cookbook[param]


def add_recipes_to_cookbook():
    new_ingredients = []
    new_ing = ""
    name = prompt("Enter a recipe name: ")
    while new_ing != "fin":
        new_ing = prompt("Enter ingredient (type fin to end): ")
        new_ingredients.append(new_ing)
    new_meal = prompt("Enter meal type: ")
    new_prep_time = prompt("Enter the prep time: ")
    new_recipe = {'ingredients': new_ingredients, 'meal': new_meal, 'prep_time': new_prep_time}
    cookbook[name] = new_recipe


if __name__ == "__main__":
    option = 0
    print("Welcome to the Python Cookbook!")
    while option != 5:
        print(
            "List of available options: "
            "\n 1:Add a recipe "
            "\n 2:Delete a recipe "
            "\n 3:Print a recipe "
            "\n 4:Print the cookbook "
            "\n 5:Quit")

        option = int(prompt("Please select an option: "))
        if option == 1:
            add_recipes_to_cookbook()
        elif option == 2:
            deleted_recipe = prompt("Indique el nombre de la receta a borrar: ")
            delete_recipe(deleted_recipe)
        elif option == 3:
            printed_recipe = prompt("Indique el nombre de la receta a imprimir: ")
            print_recipe_details(printed_recipe)
        elif option == 4:
            print_recipe_names()
