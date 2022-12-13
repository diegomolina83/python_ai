import sys

sys.path.insert(0, '../common')
import common


def sum(a, b):
    return a + b


def dif(c, d):
    return (c - d)


def prod(a, b):
    return a * b


def quot(a, b):
    return a / b


def remain(a, b):
    return a % b


if __name__ == "__main__":
    #print(common.no_arguments(sys.argv))
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print("Sum:", sum(a, b))
    print("Difference:", dif(a, b))
    print("Product:", prod(a, b))
    print("Quotient", quot(a, b))
    print("Remainder:", remain(a, b))
