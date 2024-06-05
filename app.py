from character import Player, Nurse, Boss, load_companions
from intro import create_map, print_map, random_companion_encounter, battle

print("Welcome to Jupiter. Walk around the map to get to the exit, meet companions on the way and defeat the boss at the exit to win the game!")
name = input ("Choose a name for your player:")
name = Player.name

def main():
    width, height = 10,10
    map, nurse_position = create_map(width, height)
    player = Player(0, 0)
    companions = load_companions()
    boss = Boss("DarkLord", 150, {"shadow strike": 10, "dark pulse": 30})

    while True:
        print_map(map, player)
        move = input("Enter move (up, down, left, right): ").strip().lower()
        
        if move in ['up', 'down', 'left', 'right']:
            player.move(move, map)
        else:
            print("Invalid move. Please enter 'up', 'down', 'left', or 'right'.")

        if map[player.y][player.x] == ' E ':
            if player.companion:
                print("You've reached the exit and must now face the boss!")
                battle(player.companion, boss)
                if player.companion.hp > 0:
                    print("Congratulations! You've defeated the boss and won the game!")
                else:
                    print("Your companion has fallen. You lose.")
                break
            else:
                print("You need a companion to face the boss at the exit!")
                continue
        
        if (player.y, player.x) == nurse_position:
            nurse = Nurse(nurse_position)
            nurse.heal(player.companion)
        
        if not player.companion:
            new_companion = random_companion_encounter(companions)
            if new_companion:
                print(f"You encountered a wild {new_companion.name}!")
                catch = input(f"Do you want to catch {new_companion.name}? (yes/no): ").strip().lower()
                if catch == "yes":
                    player.inventory.add_item(new_companion)
                    player.companion = new_companion
                    print(f"{new_companion.name} has joined your team!")
        
        print(f"Inventory: {[item.name for item in player.inventory.show_inventory()]}")
        if player.companion:
            print(f"Your companion: {player.companion.name} (HP: {player.companion.hp})")

if __name__ == "__main__":
    main()
