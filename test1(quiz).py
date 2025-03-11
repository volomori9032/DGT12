# quiz

score = 0

def q1():
    animal = input("What animal meows?\n cat\n dog\n rat\n : ")

    if animal == "cat":
        print("That is correct! A cat meows.")
        score = 1 + score
        print("Your current score is", score)

    elif animal == "dog" or animal == "rat":
        print("That is innocorrect! A dog barks and a rat squeaks.")

    else:
        print("That is incorrect. A cat meows.")


def q2():
    animal2 = input("What animal has a very long neck?\n giraffe\n ostrich\n squirrel\n :")

    if animal2 == "giraffe":
        print("That is correct! A giraffe has a very long neck.")
        score + 2 == score
        print("Your current score is", score)

    elif animal2 == "ostrich" or animal2 == "sqiurrel":
        print("That is innocorrect! A ostrich has a long neck, not a very long neck and a squirrel doesn't have a long neck.")

    else:
        print("That is incorrect. A giraffe has a long neck.")


def q3():
    rock1 = input("What rock is formed under heat and pressure?\n metamorphic rocks\n obsidian\n sedimentary\n :")

    if rock1 == "metamorphic rocks":
        print("That is correct! Metamorphic rocks are formed under heat and pressure.")
        score + 3 == score
        print("Your current score is", score)

    elif rock1 == "obsidian" or rock1 == "sedimentary":
        print("That is innocorrect! Obsidian is formed when volcano lava cools and sedimentary rocks are formed from pre-existing rocks or once living organisms.")

    else:
        print("That is incorrect. Metamorphic rocks are formed under heat and pressure.")


def q4():
    animal3 = input("What animal can fly?\n snowy owl\n artic fox\n polar bear\n :")

    if animal3 == "snowy owl":
        print("That is correct! A snowy owl can fly.")
        score + 4 == score
        print("Your current score is", score)

    elif animal3 == "artic fox" or animal3 == "polar bear":
        print("That is innocorrect! An artic fox is a small land animal without wings and a polar bear is a large land animal without wings.")

    else:
        print("That is incorrect. A snowy owl can fly.")
    

def q5():
    code = input("What code is used to make this quiz??\n python\n css\n html\n :")

    if code == "python":
        print("That is correct! I made this quiz with python.")
        score + 5 == score
        print("Your current score is", score)

    elif code == "css" or code == "html":
        print("That is innocorrect! A css is code to give details and apparence to html and html is used to make things like a website.")

    else:
        print("That is incorrect. I made this quiz with python.")


def quizend():
    if score == "1":
        print("Oh.. Well you tried your best! Good job.")

    elif score == "2":
        print("Well, at least you didn't get 1!")

    elif score == "3":
        print("Middle ground, good job.")

    elif score == "4":
        print("Ooh! So close.. Try again next time.")

    elif score == "5":
        print("5/5 good job.")   

    else:
        print("Oh..")


def quiz():
    
    q1()
    q2()
    q3()
    q4()
    q5()
    quizend()


name = input("What is your name I should call you by? ")
print("Hello,", name + "! I will be giving you a seris of 5 questions and you must answer each one to the best of your abilities.")
quiz()
print("Now you have finished the quiz, do you want to try again?")
tryagain = input("Yes or no")

if tryagain == "yes":
    quiz()

elif tryagain == "no":
    print("Goodbye!")

else:
    tryagain