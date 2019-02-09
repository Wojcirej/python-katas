import re

def alphabet_position(text):
    result = []
    text = re.sub('[^a-zA-Z]+', '', text).lower()
    for letter in list(text):
        result.append(str(ord(letter) - 96))
    print(" ".join(result))
    return " ".join(result)
