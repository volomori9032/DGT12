# importing easygui module
from easygui import *
 
username = enterbox("Please enter your choice of identifcation: ")
if username:
    msgbox(f"Your selected username is {username}")

else:
    msgbox("No username entered.")
