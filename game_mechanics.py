#minesweep round 2
import random
import numpy as np


x_width = 20
y_height = 20
mine_min = 50
mine_max = 100

rows = 20
cols = 20

class Cell:
    def __init__(self, mine=False, show=False, score=0, mark=0):
        self.mine = mine
        self.show = show
        self.score = score
        self.mark = mark 

    def __repr__(self):
        return f"Cell({self.mine},{self.show},{self.score},{self.mark})"


map_array_1 = [[Cell() for _ in range(cols)] for _ in range (rows)]

mine_count = random.randint(50,100)

#location of mine - boolean
full_array = np.full((x_width,y_height), False)

#reveal array - what squares are shown to player
reveal_array = np.full((x_width,y_height), False)

#heatmap of nearby mines
score_array = np.full((x_width, y_height), 0)

#placeholder
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

def check_neighbors_cell(x,y):
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
    
def local_check_cell(x,y):
    if x < 0 or x > (x_width -1):
        return False
    if y < 0 or y > (y_height -1):
        return False
    if map_array_1[x][y].mine == True:
        return True
    else:
        return False

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
            map_array_1[x_random][y_random].mine = True
            i += 1



def setup_maps():
    print("x ", x_width, " y", y_height)

    mine_count = random.randint(mine_min,mine_max)

    fill_map(mine_count)

    for j in range(y_height):
        for i in range(x_width):
            score_array[i][j] = check_neighbors(i,j)

def setup_maps_cell():
    print("for map cell array: x ", x_width, " y", y_height)

    mine_count = random.randint(mine_min,mine_max)

    fill_map(mine_count)

    for j in range(y_height):
        for i in range(x_width):
            map_array_1[i][j].score = check_neighbors_cell(i,j)

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


def print_map_details_cell():
    for j in range(y_height):
        for i in range(x_width):
            if map_array_1[i][j].mine == True:
               print("x", end="")
            else:
                print("-", end="")
        print(" |")

    print("")

    for j in range(y_height):
        for i in range(x_width):
            score = check_neighbors(i,j)
            map_array_1[i][j].score = score
            print(score, end="")
        print(" |")

def print_map():
    for j in range(y_height):
        for i in range(x_width):
            if reveal_array[i][j] == True:
                print(score_array[i][j], end="")
            else:
                print("-", end="")
        print(" |")


def print_map_cell():
    for j in range(y_height):
        for i in range(x_width):
            if map_array_1[i][j].show == True:
                print(map_array_1[i][j].score, end="")
            else:
                print("-", end="")
        print(" |")

def reveal_spread(x,y,counter):
    if x < 0 or x >= x_width:
        return
    if y < 0 or y >= y_height:
        return
    counter -= 1
    if counter <= 0:
        return
    if reveal_array[x][y] == False:
        if full_array[x][y] == False:
            reveal_array[x][y] = True
            reveal_spread(x-1,y, counter)
            reveal_spread(x+1,y, counter)
            reveal_spread(x,y-1, counter)
            reveal_spread(x,y+1, counter)

def reveal_spread_cell(x,y,counter):
    if x < 0 or x >= x_width:
        return
    if y < 0 or y >= y_height:
        return
    counter -= 1
    if counter <= 0:
        return
    if map_array_1[x][y].show == False:
        if map_array_1[x][y].mine == False:
            map_array_1[x][y].show = True
            reveal_spread_cell(x-1,y, counter)
            reveal_spread_cell(x+1,y, counter)
            reveal_spread_cell(x,y-1, counter)
            reveal_spread_cell(x,y+1, counter)

def main():

    print("x ", x_width, " y", y_height)

    setup_maps_cell()

    print_map_details_cell()

    game_loop()


def game_loop():
    player_lives = 2
    while(player_lives > 0):
        print_map_cell()
        number_valid = False
        while number_valid == False:
            x_move = int(input("x: "))
            y_move = int(input("y: "))
            print("x is : ", x_move, "y is :", y_move)
            if x_move >= 0 and x_move < x_width:
                if y_move >= 0 and y_move < y_height:
                    number_valid = True
        
        if map_array_1[x_move][y_move].mine == True:
            print("player lost")
            exit()
        else:
            #reveal_array[x_move][y_move] = True
            print("good choice")
            reveal_spread_cell(x_move,y_move,4)


    

main()