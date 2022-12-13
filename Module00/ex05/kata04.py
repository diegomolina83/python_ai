kata = (15, 4, 132.42222, 10000, 12345.67)


def normalize_kata(number):
    if number < 10:
        module = "0" + str(number)
    else:
        module = number
    return module


if __name__ == "__main__":
    print(f"module_{normalize_kata(kata[0])}, ex_{normalize_kata(kata[1])} : {round(kata[2], 2)}",
          '{0:.2e}'.format(kata[3]), '{0:.2e}'.format(kata[4]))
