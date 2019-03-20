def automorphic_number(number):
    square = number * number
    length = len(str(number))
    digits = list(map(int, str(square)))[-length:]
    if int("".join(list(map(str, digits)))) == number:
        return "Automorphic"
    else:
        return "Not!!"
