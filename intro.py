from character import Player
from character import Enemy
from character import Battle
from character import Nurse
from character import Inventory
import random 
import json


""" print ("Welcome to jupiter. Walk through the land and to the Boss to fight it. After you beat the Boss, find the exit to end the game. ")
name = input("Choose a name for your charcter:")
Player.name = name """


EMPTY = ' '
EXIT = 'E'
NURSE = 'N'
BOSS = 'B'
ANIMAL = 'A'

grid_size = 10
map_grid = [[EMPTY for _ in range(grid_size)] for _ in range(grid_size)]


exit_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
map_grid[exit_position[0]][exit_position[1]] = EXIT


nurse_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
while nurse_position == exit_position:
    nurse_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
map_grid[nurse_position[0]][nurse_position[1]] = NURSE


boss_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
while boss_position == exit_position or boss_position == nurse_position:
    boss_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
map_grid[boss_position[0]][boss_position[1]] = BOSS

num_animals = 5
animal_positions = []
for _ in range(num_animals):
    animal_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
    while animal_position == exit_position or animal_position == nurse_position or animal_position == boss_position or animal_position in animal_positions:
        animal_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
    animal_positions.append(animal_position)
    map_grid[animal_position[0]][animal_position[1]] = ANIMAL


for row in map_grid:
    print('[' + ']['.join(row) + ']')



with open('animals.json', 'r') as file:
    animals_data = json.load(file)


inventory = Inventory()
player = Player(name="nurse", health=100, inventory=inventory)
nurse = Nurse()


player_position = (0, 0)

def move_player(player_position, direction):
    x, y = player_position
    if direction == 'up' and x > 0:
        x -= 1
    elif direction == 'down' and x < grid_size - 1:
        x += 1
    elif direction == 'left' and y > 0:
        y -= 1
    elif direction == 'right' and y < grid_size - 1:
        y += 1
    return (x, y)



commands = ['down', 'down', 'right', 'right', 'up', 'right', 'down']  
for command in commands:
    player_position = move_player(player_position, command)
    x, y = player_position
    if map_grid[x][y] == NURSE:
        nurse.heal(player)
        print(f"{player.name} is healed by the nurse!")
    elif map_grid[x][y] == ANIMAL:
        animal = random.choice(animals_data)
        enemy = Enemy(name=animal['name'], health=animal['health'], attack=animal['attack'])
        battle = Battle(player, enemy)
        battle.start_battle()
    elif map_grid[x][y] == BOSS:
        boss = Enemy(name="Boss", health=150, attack=20)
        battle = Battle(player, boss)
        battle.start_battle()
        break
    elif map_grid[x][y] == EXIT:
        print(f"{player.name} has found the exit!")
        break

    print(f"Player moved to {player_position}")







    











