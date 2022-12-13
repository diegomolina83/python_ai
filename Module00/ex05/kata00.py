kata = (19, 42, 21, 45, 23, 9, 42, 567, 0)


def loop_kata(kata):
    string = ""
    for number in kata:
        string += f", {str(number)}"
    new_string = string[2:]
    return new_string


if __name__ == "__main__":
    print(f"The {len(kata)} numbers are", loop_kata(kata))
