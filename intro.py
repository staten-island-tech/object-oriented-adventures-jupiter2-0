from character import Player
import random 


""" print ("Welcome to jupiter. Walk through the land and to the Boss to fight it. After you beat the Boss, find the exit to end the game. ")
name = input("Choose a name for your charcter:")
Player.name = name"""


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
 
    map[height - 1][x] = '    E    '  

    return map

def print_maze(map, player):
    for y in range(len(map)):
        row = ""
        for x in range(len(map[y])):
            if player.x == x and player.y == y:
                row += ' P '
            else:
                row += map[y][x]
        print(row)

if __name__ == "__main__":
    width = 45
    height = 20
    
    map = create_map(width, height)
    player = Player(0, 0)

    while True:
        print_maze(map, player)
        move = input("Enter move (up, down, left, right): ").strip().lower()
        
        if move in ['up', 'down', 'left', 'right']:
            player.move(move, map)
        else:
            print("Invalid move. Please enter 'up', 'down', 'left', or 'right'.")

        if map[player.y][player.x] == ' E ':
            print("Congratulations! You've reached the exit!")
            break

    
        print(f"Inventory: {player.inventory.show_inventory()}")











