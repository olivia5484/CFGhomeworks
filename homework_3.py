
def generate_phrase(characters, phrase):
    is_match = []
    character_count = 0
    phrase_count = 0

    for i in characters:
        character_count += 1
    for j in phrase:
        phrase_count += 1

    if character_count >= phrase_count:
        for char in phrase:
            if char in characters:
                is_match.append(char)
    elif character_count == 0:
        print("Error - you have no characters! ")
        return ValueError
    else:
        print("Error - you do not have enough characters to compare words! ")
        return ValueError

    if sorted(is_match) == sorted(phrase):
        print(True)
    else:
        print(False)


generate_phrase("shdkflsahskoid", "apples")         # should return False
generate_phrase("applesasaismca", "apples")         # should return True
generate_phrase("plesasapismca", "apples")          # should return True
generate_phrase("plesasapismca", "apples!")         # should return False
generate_phrase("absh", "apples")                   # should return not enough characters error
generate_phrase("", "apples")                       # should return empty characters error
generate_phrase("asfgdfsg", " ")                    # should return False - no space in characters
generate_phrase("dh qaks !2", " ")                  # should return True - as there is a white space in both
generate_phrase("dh qaks !2", "! ")                 # should return True

