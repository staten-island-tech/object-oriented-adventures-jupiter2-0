print("Welcome to __. This is the begining of your journey. Catch and level up to defeat bosses. The final goal of your journey is to defeat the final boss.")
name = input("Choose a name for your charcter:")
player = name

while True:
    inven = input("Do you want to check your inventory?")
    if inven.lower == 'no':
        break
    

print("These are you're starter pets.")

class character:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def move (self, direction):
    if direction == "up":
        self.y += 1
    elif direction == "down":
        self.y -= 1
    elif direction == "left":
        self.x -= 1
        


    
    
