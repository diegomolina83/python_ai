from recipe import Recipe
from book import Book

if __name__ == "__main__":
    recipe = Recipe("Tortilla de patatas", 5, 15, ["patatas", "huevos", "sal", "cebolla", "aciete"],
                    "lunch", "La madre de todas las comidas")
    to_print = str(recipe)
    print(to_print)

    new_book = Book("Recetas españolas", 12 / 12 / 2022, 12 / 12 / 2022, recipe)

    print("Nombre del libro de recetas: ", new_book.name)
