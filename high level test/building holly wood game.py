x=2
y=1

while int(x)!=int(y):

    from math import *

    def cls():

        print("/n" * 100)

    word_type=""
    hint_holly_word=""
    holly_word=""
    word=""

    message = "please enter your word:"
    losing_message = "you are wrong try again"
    victory_message = "you are correct"

    word_type = input("please enter the type of holly_word:")
    holly_word = input("second player " + message)
    print(str(floor((len(holly_word)) // 3)) + " This is the number of hints you have to enter")
    hint_holly_word = input("type one hint letter for every 3 letters of the word:")

    print("\n" * 1000)
    while holly_word.upper() != word.upper():
        print("\t\t\t\t\t" + word_type)
        print(hint_holly_word + "\n\n")
        word = input(message)

    print(victory_message)
    y=input("\ndo you want to exit (1=no,2=yes)")
    int(y)