txt = "house"
VOWELS = "AEIOU"
CONSONANTS= "BCDFGHJKLMNPQRSTVWXYZ"

for text in txt:
    if text.upper() in VOWELS:
        print(text, end="")
    else:
        print("")
        