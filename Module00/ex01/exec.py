import sys


def hello(a):
    print("hello", a)


def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


if __name__ == "__main__":
    cadena = ''
    if len(sys.argv) <= 1:
        print("Necesitamos más argumentos")
    else:
        for x in sys.argv[1:]:
            cadena = cadena + " " + x
        hello(reverse(cadena).swapcase())
