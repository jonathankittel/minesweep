#minesweep round 2
import random
import numpy as np

x_width = 30
y_height = 30

print("x ", x_width, " y", y_height)

mine_count = random.randint(10,20)


bool_array = np.array([True, False, True, False])

full_array = np.full((x_width,y_height), False)

i = 0
while i < mine_count:
    x_random = random.randint(0,30)
    y_random = random.randint(0,30)
    full_array[x_random][y_random] = True
    i += 1

print(bool_array)

count = 0
i = 0
j = 0
while j < y_height:
    while j < x_width:
        if full_array[i][j] == True:
            print("x", end="")
        else:
            print("-", end="")
        count += 1
        j += 1
    print(" |")
    j = 0
    i += 1



print("count ", count)
print(mine_count)

