# TEST ONE

"""
name = input("Enter User: ")
print("The user you have chosen is", name, ".")

yes = input("Do you wish to chose a different one?")

if yes == "no":
    print("Well then,", name, "is your final choice of user.")

elif "no":
    name = input("Enter User: ")
    print("The user you have chosen is", name, ".")
"""

# TEST TWO

"""
score = 5

def user():
    
    global name
    name = input("Enter User: ")
    print("The user you have chosen is", name, ".")
    yn = input("Do you wish to chose a different one?\n Yes\n No\n : ")

    if yn == "no":
        print("Well then,", name, "is your final choice of user.")
        score = score + 10

    elif yn == "yes":
        name = input("Enter User: ")
        print("The user you have chosen is", name, ".")
        yn = input("Do you wish to chose a different one?\n Yes\n No\n : ")

    else:
        print("You have encountered an Error. Please try again and follow intructions.")


if score == 5:
    user()
"""

# TEST 3

score = 5

def user():
    
    global name
    name = input("Enter User: ")
    print(f"The user you have chosen is {name} .")
    yn = input("Do you wish to chose a different one?\n Yes\n No\n : ")

    if yn == "no":
        print(f"Well then, {name} is your final choice of user.")
        score = score + 10

    elif yn == "yes":
        name = input("Enter User: ")
        print(f"The user you have chosen is {name} .")
        yn = input("Do you wish to chose a different one?\n Yes\n No\n : ")

    else:
        print("You have encountered an Error. Please try again and follow intructions.")


if score == 5:
    user()