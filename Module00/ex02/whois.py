import sys


def is_even_or_odd(number):
    if (number==0):
        print("El número es un cero")
    elif (number % 2 != 0):
        print("El número es impar")
    else:
        print("El número es par")


if __name__ == "__main__":
    numero = 0;
    if(not sys.argv[1].isnumeric()):
        print("No es un número")
    elif len(sys.argv) <= 1 or len(sys.argv) > 2:
        print("Número incorrecto de argumentos")
    else:
        is_even_or_odd(int(sys.argv[1]))
