def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "o"
        else:
            translation = translation + letter

    print(translation)

translate("This is Sparta")
