#minesweep round 2
import random
import numpy as np


x_width = 20
y_height = 20
mine_min = 50
mine_max = 100

mine_count = random.randint(50,100)

full_array = np.full((x_width,y_height), False)

reveal_array = np.full((x_width,y_height), False)

score_array = np.full((x_width, y_height), 0)

marker_array = np.full((x_width, y_height), " ")

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
    
def fill_map(mine_count):
    i = 0
    while i < mine_count:
        x_random = random.randint(0,(x_width - 1))
        y_random = random.randint(0,(y_height - 1))
        if full_array[x_random][y_random] == False:
            full_array[x_random][y_random] = True
            i += 1


def setup_maps():
    print("x ", x_width, " y", y_height)

    mine_count = random.randint(mine_min,mine_max)

    fill_map(mine_count)

    for j in range(y_height):
        for i in range(x_width):
            score_array[i][j] = check_neighbors(i,j)


def print_map_details():
    for j in range(y_height):
        for i in range(x_width):
            if full_array[i][j] == True:
               print("x", end="")
            else:
                print("-", end="")
        print(" |")

    print("")

    for j in range(y_height):
        for i in range(x_width):
            score_array[i][j] = check_neighbors(i,j)
            print(score_array[i][j], end="")
        print(" |")

def print_map():
    for j in range(y_height):
        for i in range(x_width):
            if reveal_array[i][j] == True:
                print(score_array[i][j], end="")
            else:
                print("-", end="")
        print(" |")




def main():

    print("x ", x_width, " y", y_height)

    setup_maps()

    print_map_details()

    game_loop()


def game_loop():
    player_lives = 2
    while(player_lives > 0):
        print_map()
        number_valid = False
        while number_valid == False:
            x_move = int(input("x: "))
            y_move = int(input("y: "))
            print("x is : ", x_move, "y is :", y_move)
            if x_move >= 0 and x_move < x_width:
                if y_move >= 0 and y_move < y_height:
                    number_valid = True
            
        if full_array[x_move][y_move] == True:
            print("player lost")
            exit()
        else:
            reveal_array[x_move][y_move] = True
            print("good choice")


    

main()