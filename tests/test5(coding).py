# importing easygui module
from easygui import *

def exit():
    quit = buttonbox("Do you wish to quit?", title = "Quit?", choices = ["Continue", "Quit"])
    if quit == "continue":
        pass
    else:
        quit

def userselector():

    username = enterbox(msg = "Please enter your choice of identifcation:\n If you wish to not proceed, do not enter a user.", title = "Username selector.")
    if username:
        if ccbox(msg = f"Please confirm you wish, {username}, as your user."): 
            pass
            msgbox(msg = f"Your user is {username}.", title = "Selected user.")
        else:
            exit()
            userselector()
        

    else:
        quit = buttonbox("No username entered\n Do you wish to choose a user or quit?", title = "Quit?", choices = ["Choose user", "Quit"])
        if quit == "Choose user":
            userselector()
        
        elif quit == "quit":
            quit

        else:
            quit

    

userselector()