import sys


def filterwords(argv, num):
    words = []
    word = ""
    count = 0

    for character in argv:
        count += 1
        if not character.isspace():
            word += character
        else:
            words.append(word)
            word = ""
    if count == len(argv):
        words.append(word)
    newlist = [word for word in words if len(word) > int(num)]
    print(newlist)


if __name__ == "__main__":
    if sys.argv[1].isnumeric():
        print("el primer argumento debe ser una cadena de texto")
    if not sys.argv[2].isnumeric():
        print("El segundo argumento debe ser un numero")
    else:
        filterwords(sys.argv[1], sys.argv[2])
