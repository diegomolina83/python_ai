import sys

from prompt_toolkit import prompt


def text_analyzer(string=""):
    """Esta función cuenta las minúsculas, mayúsculas puntos y espacios de una cadena de texto"""
    lower_letters = upper_letters = punctuation_marks = spaces = characters = 0
    if len(string) == 0:
        string = prompt("Give me a text:")
    for character in string:
        characters += 1
        if character.islower():
            lower_letters += 1
        elif character.isupper():
            upper_letters += 1
        elif character.isspace():
            spaces += 1
        elif character == "." or "," or ":" or ";":
            punctuation_marks += 1
    print_results(characters, upper_letters, lower_letters, punctuation_marks, spaces)


def print_results(char, upper, lower, punctuation, spaces):
    print(f"The text contains {char} character(s): ")
    print(f"-{upper} upper letter(s)")
    print(f"-{lower} lower letter(s)")
    print(f"-{punctuation} punctuation marks")
    print(f"-{spaces} space(s)")


if __name__ == "__main__":
    if len(sys.argv[0:]) > 2:
        print("Introduce solo una string")
    else:
        text_analyzer(sys.argv[1])
