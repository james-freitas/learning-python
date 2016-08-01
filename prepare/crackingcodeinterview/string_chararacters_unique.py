def unique(input):
    unique_chars = set()
    for character in input:
        if character in unique_chars:
            return False
        unique_chars.add(character)
    return True

if unique("Alabama"):
    print "it is unique"
else:
    print "it is not unique"
