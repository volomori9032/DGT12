# quiz


def quiz():

    global score
    score = 0
    q1()
    q2()
    q3()
    q4()
    q5()
    answerchecker()
    
def q1():

    global score
    score1 = 0
    num1 = input("What is 5 + 5?: ")

    if num1 == "10":
        score1 = score1 + 1
        score = score1 + score
        print(f"You are correct, well done. Your current score is {score}.")

    elif num1.isalpha():
        print(f"Why are you using letters in a math question? Your current score is {score}.")

    else:
        print(f"Incorrect. Answer is 10. Your current score is {score}.")

def q2():

    global score
    score2 = 0
    num2 = input("What is 5 + 4?: ")

    if num2 == "9":
        score2 = score2 + 1
        score = score + score2
        print(f"You are correct, well done. Your current score is {score}.")

    elif num2.isalpha():
        print(f"Why are you using letters in a math question? Your current score is {score}.")

    else:
        print(f"Incorrect. Answer is 9. Your current score is {score}.")

def q3():

    global score
    score3 = 0
    num3 = input("What is 3 + 6?: ")

    if num3 == "9":
        score3 = score3 + 1
        score = score + score3
        print(f"You are correct, well done. Your current score is {score}.")

    elif num3.isalpha():
        print(f"Why are you using letters in a math question? Your current score is {score}.")

    else:
        print(f"Incorrect. Answer is 9. Your current score is {score}.")

def q4():

    global score
    score4 = 0
    num4 = input("What is 2 + 7?: ")

    if num4 == "9":
        score4 = score4 + 1
        score = score + score4
        print(f"You are correct, well done. Your current score is {score}.")

    elif num4.isalpha():
        print(f"Why are you using letters in a math question? Your current score is {score}.")

    else:
        print(f"Incorrect. Answer is 9. Your current score is {score}.")

def q5():

    global score
    score5 = 0
    num5 = input("What is 1 + 8?: ")

    if num5 == "9":
        score5 = score5 + 1
        score = score + score5
        print(f"You are correct, well done. Your current score is {score}.")

    elif num5.isalpha():
        print(f"Why are you using letters in a math question? Your current score is {score}.")

    else:
        print(f"Incorrect. Answer is 9. Your current score is {score}.")

def answerchecker():
    if score == 1:
        print(f"You got {score} out of 5 which is {score * 100} as a percentage")
        print("Oh.. Well you tried your best! Good job.")

    elif score == 2:
        print(f"You got {score} out of 5 which is {score * 100} as a percentage")
        print("Well, at least you didn't get 1!")

    elif score == 3:
        print(f"You got {score} out of 5 which is {score * 100} as a percentage")
        print("Middle ground, good job.")

    elif score == 4:
        print(f"You got {score} out of 5 which is {score * 100} as a percentage")
        print("Ooh! So close.. Try again next time.")

    elif score == 5:
        print(f"You got {score} out of 5 which is {score * 100} as a percentage")
        print("5/5 good job.")   

    else:
        print(f"You got {score} out of 5 which is {score * 100} as a percentage")
        print("Oh..")

    
quiz()