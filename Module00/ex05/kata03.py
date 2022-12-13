kata = "The right format asereje "


if __name__ == "__main__":
    number = 41 - len(kata)
    string = ""
    while number > 0:
        string += "-"
        number -= 1
    print(f"{string}{kata}")

