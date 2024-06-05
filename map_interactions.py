<<<<<<< HEAD:intro.py

=======
>>>>>>> a032d00f00319e6b116779fba7e8fb40fb714dad:map_interactions.py
from character import Player
from character import Inventory
import random 
import json
<<<<<<< HEAD:intro.py
load_companion = open("./companion.json", encoding="utf8")
data = json.load(load_companion)
=======
>>>>>>> a032d00f00319e6b116779fba7e8fb40fb714dad:map_interactions.py

""" print ("Welcome to jupiter. Walk through the land and to the Boss to fight it. After you beat the Boss, find the exit to end the game. ")
name = input("Choose a name for your charcter:")
Player.name = name"""

def create_map(width, height):
    map = [['[ ]' for _ in range(width)] for _ in range(height)]
<<<<<<< HEAD:intro.py
    
    
    x, y = 0, 0
    map[y][x] = '[S]' 
    
=======

    if __name__ == "__main__":
        num_companions = 12
        width = 45
        height = 20
        companions = []
        companion_positions = set()
        while len(companion_positions) < num_companions:
            ax, ay = random.randint(0, width - 1), random.randint(0, height - 1)
            if map[ay][ax] == '   ' and (ax, ay) != (0, 0):
                companion_positions.add((ax, ay))
                map[ay][ax] = ' A '

    return map, companion_positions

def print_map(map, player):
    for y in range(len(map)):
        row = ""
        for x in range(len(map[y])):
            if player.x == x and player.y == y:
                row += ' P '
            else:
                row += map[y][x]
        print(row)

def check_for_animal(player, companion_positions, inventory):
    pos = player.get_position()
    if pos in companion_positions:
        companion = random.choice([])
        inventory.add_item(companion)
        print(f"You encountered a {companion} and added it to your inventory!")
        companion_positions.remove(pos)


    num_companions = 12
    map, companion = create_map(width, height, num_companions)
    player = Player(0, 0)

    while True:
        print_map(map, player)
        move = input("Enter move (up, down, left, right): ").strip().lower()
        
        if move in ['up', 'down', 'left', 'right']:
            player.move(move, map)
            check_for_animal(player, companion_positions, player.inventory)
        else:
            print("Invalid move. Please enter 'up', 'down', 'left', or 'right'.")

        if map[player.y][player.x] == ' E ':
            print("Congratulations! You've reached the exit!")
            break

        print(f"Inventory: {player.inventory.show_inventory()}")

def create_map(width, height):
    map = [['[ ]' for _ in range(width)] for _ in range(height)]

    x, y = 0, 0
    map[y][x] = '[S]'

>>>>>>> a032d00f00319e6b116779fba7e8fb40fb714dad:map_interactions.py
    while y < height - 1:
        direction = random.choice(['down', 'right'])
        if direction == 'down' and y < height - 1:
            y += 1
        elif direction == 'right' and x < width - 1:
            x += 1
<<<<<<< HEAD:intro.py
        map[y][x] = '   '  

 
=======
            map[y][x] = '   '  
>>>>>>> a032d00f00319e6b116779fba7e8fb40fb714dad:map_interactions.py
    map[height - 1][x] = '     E     '  

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

def encounter_companion(companion):
    if random.random() < 0.4:  
        return random.choice(companion)
    return None

if __name__ == "__main__":
    width = 45
    height = 20 
    
<<<<<<< HEAD:intro.py
    maze = create_map(width, height)
=======
    map = create_map(width, height)

>>>>>>> a032d00f00319e6b116779fba7e8fb40fb714dad:map_interactions.py
    player = Player(0, 0)
    companion = load_companion('Companion.json')

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

        
        companion = encounter_companion(companion)
        if companion:
            print(f"You've encountered a {companion}!")
            player.inventory.add_item(companion)

<<<<<<< HEAD:intro.py
        
        print(f"Inventory: {player.inventory.show_inventory()}") 
=======





>>>>>>> a032d00f00319e6b116779fba7e8fb40fb714dad:map_interactions.py
