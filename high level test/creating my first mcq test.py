from Question_class import Questionit

Question_paper = [
    "Which one is the largest shark?\n(a):Whale shark\n(b):Great White shark\n(c):Tiger shark\n\n",
    "Which one is the largest animal?\n(a):argentinosaurus\n(b):titanaboa\n(c):blue whale\n\n",
    "Which one wqs the biggest empire?\n(a):ottoman empire\n(b):british empire\n(c):mongal empire\n\n"
]
Question_1 = [
    Questionit(Question_paper[0], "a"),
    Questionit(Question_paper[1], "a"),
    Questionit(Question_paper[2], "c"),
]


def Question_func(Questions) :
    score = 0
    varying_number = 0

    for Looping_Question in Questions :
        Answer = input(Question_1[varying_number].Question_prompt)
        if Answer == Question_1[varying_number].Answer :
            score += 1
        varying_number += 1
    print("you got " + str(score) + "/" + str(len(Questions)))
Question_func(Question_1)
