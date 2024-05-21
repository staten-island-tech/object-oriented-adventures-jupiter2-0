import player
import inventory 

print ("Welcome to jupiter. Walk through the land and to the Boss to fight it. After you beat the Boss, find the exit to end the game. ")
name = input("Choose a name for your charcter:")
player = name
inven = input("Do you want to check your inventory? ")
if inven == "yes":
    open inventory
if inven == "no":
    exit


input("Do you want to move up, down, left or right:")

def movement():
    player.move
    




