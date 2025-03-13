# Game

score = 5


def user():
    
    global name
    global score
    name = input("Please enter your user: ")
    print(f"The user you have chosen is {name}.")
    yn = input("Do you wish to chose a different one?\n Yes\n No\n : ").upper().lower()

    if yn == "no":
        print(f"Well then, {name} is your final choice of user.")
        score = score + 10

    elif yn == "yes":
        name = input("Enter User: ")
        print(f"The user you have chosen is {name}.")
        yn = input("Do you wish to chose a different one?\n Yes\n No\n : ")

    else:
        print("You have encountered an Error. Please try again and follow intructions.")
        user()


def world():

    print(f"Welcome traveler, {name}!")
    print("Your current setting is Mythpond Forest. Lastbrook, Angelbreak. Mythpond forest is a forest spanning 5.8  million square kilometres.")
    print("This forest is known to be extremely dangerous and be inhabited by a few mythical creatures, those of which are only persumed to be in legends or old folk lore,")
    print("Though that is just what the elders say, you don't have to believe them. They probably only misremember what they saw in there or were hallucinating.")
    print("Anyways, the trees here are GIANT, like 2km tall on average so once you get into it there ain't any sunlight unless the trees are far and between or loose leaves.")
    
    gameentry1()    


def gameentry1():

    print("You have been tasked to enter the forest and find a missing couple who have been missing for 4 months now.")
    print("The reward for completing the mission is 10 milion dollars.")
    gameentry = input("""
                    Do you accept?\n
                    Yes\n
                    No\n
                     : """).upper().lower()
    
    if gameentry == "yes":
        print("Very well then traveler, I wish you the very best of luck with your adventure.")

    elif gameentry == "no":
        print("Very well then traveler, I hope to see you in the future.")

    else:
        print("You have entered something other than what you have been provided with, I assume this is a mistake. I will give you the decision again.")
        gameentry2 = ("""
                    Do you wish to accept the mission?\n
                    Yes\n
                    No\n
                     : """)
        
        if gameentry2 == "yes":
            print("Very well then traveler, I wish you the very best of luck with your adventure.")

        elif gameentry2 == "no":
            print("Very well then traveler, I hope to see you in the future.")

        else:
            print("I take this as you wishing to not accept the mission, goodbye traveler.")


def characterclasses():

    global characterclass
    print("Before you start on your quest traveler, please select a class you wish to play as within the forest.")

    mageweapons = ["Spells Book", "Spells Staff"]
    summonerpets = ["Cat", "Dog", "Wolf", "Slime"]
    meleeweapons = ["Long sword", "Short sword", "Dagger"]
    characterclass = input("Please select a class out of this selection.\n Ranger, Melee, Summoner, Mage\n : ").upper().lower()
    
    if characterclass == "ranger":
        ranger()

def ranger():

    global arrows
    global bullets
    arrows = 0
    bullets = 0

    print("Ah, a bow or gun user hm? Good luck.")
    rangerweapon = input("Please choose which weapon type you would like:\n Gun, Bow\n : ").upper().lower()

    if rangerweapon == "gun":
        print("Ah! Guns. You must be a interesting person.\n Heres a gun and 100 bullets, use them sparely until you can buy more.")
        bullets = bullets + 100

    elif rangerweapon == "bow":
        print("Ah! A bow, you must have good strength.\n Heres a bow and 100 arrows, use them sparely until you can buy more.")
        arrows = arrows + 100

    else:
        print("Please pick a weapon. Input a choice, not somthing else.")
        ranger()

# within this area is for testing only



# Below this is how it should go in order

if score == 5:
    user()

world()
characterclasses()
