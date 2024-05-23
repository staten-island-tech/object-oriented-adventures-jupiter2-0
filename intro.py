from character import Player
import random 

print ("Welcome to jupiter. Walk through the land and to the Boss to fight it. After you beat the Boss, find the exit to end the game. ")
name = input("Choose a name for your charcter:")
Player.name = name


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
        map[y][x] = ''
    
    map[height - 1][x] = '       E       '
    return map

def print_map(map, player):
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if (x, y) == player.get_position():
                print('[P]', end='')
            else:
                print(cell, end='')
        print()

def main():
    width, height = 40, 5
    map = create_map(width, height)
    player = Player()

    while True:
        print_map(map, player)
        action = input("Do you want to check your inventory? (yes/no): ").strip().lower()
        
        if action == 'yes':
            player.inventory.show_inventory()
        else:
            direction = input("Where do you want to go? (up/down/left/right): ").strip().lower()
            player.move(direction)
            print()

if __name__ == "__main__":
    main()



