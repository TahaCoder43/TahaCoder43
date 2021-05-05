def translate(phrase):
    translation=""
    for letter in phrase:
        if letter.lower in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    print(translation)
    return (translation)

phrase=input("enter your word to be translated:  ")

translate(phrase)