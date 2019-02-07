def abbreviate_two_word_name(name):
    abbrev = []
    for word in name.split(" "):
        abbrev.append(word[0].upper())
    return ".".join(abbrev)
