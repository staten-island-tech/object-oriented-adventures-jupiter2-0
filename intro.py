<<<<<<< HEAD
from character import Player
from character import Inventory
import random 
import json


<<<<<<< HEAD
<<<<<<< HEAD
print("Welcome to __. This is the begining of your journey. Catch and level up to defeat bosses. The final goal of your journey is to defeat the final boss.")
name = input("Choose a name for your charcter:")
player = name

while True:
    inven = input("Do you want to check your inventory?")
    if inven.lower == 'no':
        break
    

print("These are you're starter pets.")

def move (self, direction):
    if direction == "up":
        self.y += 1
    elif direction == "down":
        self.y -= 1
    elif direction == "left":
        self.x -= 1
    elif direction == "right":
        self.x += 1

def main():
    player = player(0,0)

while True:
    user_input = input("right/ left/ up/ down:")
    if user_input in ["right, left, up, down"]:
        player.move(user_input)


=======
=======
>>>>>>> e3564a9f1b9f3550e25826c624ae2cf83605aa36
""" print ("Welcome to jupiter. Walk through the land and to the Boss to fight it. After you beat the Boss, find the exit to end the game. ")
name = input("Choose a name for your charcter:")
Player.name = name """


def create_map(width, height):
    map = [['[ ]' for _ in range(width)] for _ in range(height)]

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
    
    while y < height - 1:
        direction = random.choice(['down', 'right'])
        if direction == 'down' and y < height - 1:
            y += 1
        elif direction == 'right' and x < width - 1:
            x += 1
        map[y][x] = '   '  
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

def load_companions(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['companion']

def encounter_companion(companions):
    if random.random() < 0.3: 
        return random.choice(companions)
    return None

if __name__ == "__main__":
    width = 45
    height = 20  
    
    map = create_map(width, height)
    player = Player(0, 0)
    companions = load_companions('companion.json')

    while True:
        print_map(map, player)
        move = input("Enter move (up, down, left, right): ").strip().lower()
        
        if move in ['up', 'down', 'left', 'right']:
            player.move(move, map)
        else:
            print("Invalid move. Please enter 'up', 'down', 'left', or 'right'.")

        if map[player.y][player.x] == '     E     ':
            print("Congratulations! You've reached the exit!")
            break

    
        companion = encounter_companion(companions)
        if companion:
            print(f"You've encountered a {companion}!")
            player.inventory.add_item(companion)




    








<<<<<<< HEAD
>>>>>>> vicky
=======
=======
import json


print("Welcome to __. This is the begining of your journey. Catch and level up to defeat bosses. The final goal of your journey is to defeat the final boss.")
name = input("Choose a name for your charcter:")
player = name

while True:
    inven = input("Do you want to check your inventory?")
    if inven.lower == 'no':
        break
    

print("These are you're starter pets.")

def move (self, direction):
    if direction == "up":
        self.y += 1
    elif direction == "down":
        self.y -= 1
    elif direction == "left":
        self.x -= 1
    elif direction == "right":
        self.x += 1

def main():
    player = player(0,0)

while True:
    user_input = input("right/ left/ up/ down:")
    if user_input in ["right, left, up, down"]:
        player.move(user_input)


>>>>>>> 4c16a68c459185d221a2d36f0c14b113d9a88d17
>>>>>>> e3564a9f1b9f3550e25826c624ae2cf83605aa36



