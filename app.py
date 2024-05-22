<<<<<<< HEAD

width = 45
height = 20

map = [['[ ]' for _ in range(width)] for _ in range(height)]
import random

def create_map(map, start_x, start_y):
    stack = [(start_x, start_y)]
    map[start_y][start_x] = '' 
    
    while stack:
        x, y = stack[-1]
        directions = [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2)]
        random.shuffle(directions)
        
        for (new_x, new_y) in directions:
            if 0 <= new_x < width and 0 <= new_y < height and map[new_y][new_x] == '[]':
                map[(y + new_y) // 2][(x + new_x) // 2] = '' 
                map[new_y][new_x] = ''  
                stack.append((new_x, new_y))
                break
        else:
            stack.pop() 
create_map(map, 1, 1)
def print_map(map):
    for row in map:
        print(''.join(row))

print_map(map)



=======
>>>>>>> b19e4886b5805412f62304797be575cbd4b1ff51
