from character import Player
from character import Companion
from character import Enemy
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

def load_animals(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['animals']

def encounter_animal(animals):
    if random.random() < 0.4:  
        return random.choice(animals)
    return None

def encounter_companion():
    if random.random() < 0.4: 
        return companion()
    return None

def encounter_nurse():
    print("You have encountered a nurse. She says:")
    print("'Hello there! I can heal you and your companions.'")
    print("'Be careful in this map, and good luck!'")

if __name__ == "__main__":
    width = 45
    height = 20
    
    map = create_map(width, height)
    player = Player(health=100, attack_power=20, start_x=0, start_y=0)
    animals = load_animals('animals.json')

    while True:
        print_map(map, player)
        move = input("Enter move (up, down, left, right): ").strip().lower()
        
        if move in ['up', 'down', 'left', 'right']:
            player.move(move, map)
        else:
            print("Invalid move. Please enter 'up', 'down', 'left', or 'right'.")

        if map[player.y][player.x] == ' E ':
            print("Congratulations! You've reached the exit!")
            break
        elif map[player.y][player.x] == ' N ':
            encounter_nurse()
        
   
        animal = encounter_animal(animals)
        if animal:
            print(f"You've encountered a {animal}!")
            player.inventory.add_item(animal)

       
        companion = encounter_companion()
        if companion:
            print(f"You've met {Companion.name} who will join you on your journey!")
            player.inventory.append(companion)


        if random.random() < 0.2:
            enemy = Enemy(health = 50, attack_power = 15)
            Battle(player, enemy)
            if not Player.alive():
                print("Game Over")
                break

        print(f"Inventory: {player.inventory.show_inventory()}")
        print(f"Companions: {[Companion.name for companion in Player.companions]}")





    











