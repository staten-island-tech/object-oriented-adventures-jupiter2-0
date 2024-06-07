import random
from character import Player


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

    nurse_position = (random.randint(1, height-2), random.randint(1, width-2))
    map[nurse_position[0]][nurse_position[1]] = '[N]'

    return map, nurse_position

def print_map(map, player):
    for y in range(len(map)):
        row = ""
        for x in range(len(map[y])):
            if player.x == x and player.y == y:
                row += ' P '
            else:
                row += map[y][x]
        print(row)

def random_companion_encounter(companions):
    return random.choice(companions) if random.randint(0, 10) < 6 else None

def battle(player_companion, boss):
    while player_companion.hp > 0 and boss.hp > 0:
        print(f"Your companion's HP: {player_companion.hp}")
        print(f"Boss's HP: {boss.hp}")
        
        move = input(f"Choose an attack {list(player_companion.attacks.keys())}: ").strip().lower()
        if move in player_companion.attacks:
            boss.hp -= player_companion.attack(move)
            print(f"{player_companion.name} used {move}! Boss HP is now {boss.hp}")
        
        if boss.hp > 0:
            boss_move = random.choice(list(boss.attacks.keys()))
            player_companion.hp -= boss.attack(boss_move)
            print(f"Boss used {boss_move}! {player_companion.name}'s HP is now {player_companion.hp}")
        
        if player_companion.hp <= 10:
            use_potion = input("Your companion is low on HP! Use a potion? (yes/no): ").strip().lower()
            if use_potion == "yes":
                Player.inventory.use_potion(player_companion)
        






    











    





