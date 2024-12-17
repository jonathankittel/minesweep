#minesweep round 2
import random
import numpy as np



def check_neighbors(x,y):
    score = 0
    score += local_check((x-1), (y-1))
    score += local_check(x, (y-1))
    score += local_check((x+1), (y-1))

    score += local_check((x-1), y)
    score += local_check((x+1), y)

    score += local_check((x-1), (y+1))
    score += local_check(x, (y+1))
    score += local_check((x+1), (y+1))

    return score

    
def local_check(x,y):
    if x < 0 or x > (x_width -1):
        return False
    if y < 0 or y > (y_height -1):
        return False
    if full_array[x][y] == True:
        return True
    else:
        return False

x_width = 20
y_height = 20

print("x ", x_width, " y", y_height)

mine_count = random.randint(50,100)


bool_array = np.array([True, False, True, False])

full_array = np.full((x_width,y_height), False)

score_array = np.full((x_width, y_height), 0)

i = 0
while i < mine_count:
    x_random = random.randint(0,(x_width - 1))
    y_random = random.randint(0,(y_height - 1))
    if full_array[x_random][y_random] == False:
        full_array[x_random][y_random] = True
        i += 1

print(bool_array)

count = 0
x = 0
y = 0
while y < y_height:
    while x < x_width:
        if full_array[x][y] == True:
            print("x", end="")
        else:
            print("-", end="")
        count += 1
        x += 1
    print(" |")
    x = 0
    y += 1

count = 0
x = 0
y = 0
while y < y_height:
    while x < x_width:
        score_array[x][y] = check_neighbors(x,y)
        print(score_array[x][y], end="")
        count += 1
        x += 1
    print(" |")
    x = 0
    y += 1





print("count ", count)
print(mine_count)

