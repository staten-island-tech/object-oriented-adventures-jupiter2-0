from character import Player
from character import Enemy
from character import Inventory
from character import Battle
import random 
import json

""" print ("Welcome to jupiter. Walk through the land and to the Boss to fight it. After you beat the Boss, find the exit to end the game. ")
name = input("Choose a name for your charcter:")
Player.name = name """


def create_map(width, height):
    map = [['[ ]' for _ in range(width)] for _ in range(height)]
    
    x, y = 0, 0
    map[y][x] = '[S]'  
    
    while y < height - 1:
        direction = random.choice(['down', 'right'])
        if direction == 'down' and y < height - 1:
            y += 1
        elif direction == 'right' and x < width - 1:
            x += 1
        map[y][x] = '   '  

    
    map[height - 1][x] = ' E '  

    
    while True:
        nx, ny = random.randint(0, width - 1), random.randint(0, height - 1)
        if map[ny][nx] == '   ':
            map[ny][nx] = ' N '  
            break

    return map

def print_map(map, player):
    for y in range(len(map)):
        row = ""
        for x in range(len(map[y])):
            if player.x == x and player.y == y:
                row += ' P '
            else:
                row += map[y][x]
        print(row)

def load_companions():
    with open("companion.json", 'r') as file:
        companions = json.load(file)
    return companions

def encounter_animal(animals):
    if random.random() < 0.4: 
        return random.choice(animals)
    return None

def encounter_companion(companions):
    if random.random() < 0.2:  
        comp = random.choice(companions)
        return companion(name=comp["name"], attack_power=comp["attack_power"])
    return None

def encounter_nurse(player):
    print("You have encountered a nurse. She says:")
    print("'Hello there! I can heal you and your companions.'")
    player.health = 100  
    for companion in player.companions:
        companion.health = 100  
    print("All your companions have been healed to full health.")

if __name__ == "__main__":
    width = 45  
    height = 20
    
    maze = create_map(width, height)
    player = Player(start_x=0, start_y=0)
    companions = load_companions()
    companion = ['Hydro, Wisp, Coralwhirl, Sylphire, Infernite, Emberix, Floridance']

    while True:
        print_map(map, player)
        move = input("Enter move (up, down, left, right): ").strip().lower()
        
        if move in ['up', 'down', 'left', 'right']:
            player.move(move, map)
        else:
            print("Invalid move. Please enter 'up', 'down', 'left', or 'right'.")

        if map[player.y][player.x] == ' E ':
            boss = Enemy(name="Boss", health=50, attack_power=25)
            print("You've reached the exit, but a boss blocks your way!")
            Battle(companion, boss)
            if companion.is_alive():
                print("Congratulations! You've defeated the boss and escaped the maze!")
            else:
                print("Game Over. You were defeated by the boss.")
            break
        elif map[player.y][player.x] == ' N ':
            encounter_nurse(player)
     
        animal = encounter_animal(companion)
        if animal:
            print(f"You've encountered a {animal}!")
            player.inventory.add_item(animal)

        
        companion = encounter_companion(companions)
        if companion:
            print(f"You've met {companion.name} who will join you on your journey!")
            player.companions.append(companion)


        if random.random() < 0.1: 
            enemy = Enemy(name="", health=10, attack_power=5)
            Battle(companion, enemy)
            if not companion.is_alive():
                print("Game Over")
                break

        
        items, potions = player.invenotry.show_inventory()
        print(f"Inventory: {items}, Potions: {potions}")
        print(f"Companions: {[comp.name for comp in player.companions]}")







    





