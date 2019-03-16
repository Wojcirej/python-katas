def rot_13(message):
    result = []
    for char in message:
        if is_small_letter(char):
            result.append(chr((ord(char) + 13 - 65) % 26 + 65))
        elif is_capital_letter(char):
            result.append(chr((ord(char) + 13 - 97) % 26 + 97))
        else:
            result.append(char)
    return "".join(result)

def is_small_letter(char):
    if 65 <= ord(char) <= 90:
        return True
    return False

def is_capital_letter(char):
    if 97 <= ord(char) <= 122:
        return True
    return False
