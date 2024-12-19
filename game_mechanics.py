#minesweep round 2
import random
import numpy as np





class Cell:
    def __init__(self, mine=False, show=False, score=0, mark=0):
        self.mine = mine
        self.show = show
        self.score = score
        self.mark = mark 

    def __repr__(self):
        return f"Cell({self.mine},{self.show},{self.score},{self.mark})"


class Game:

    def __init__(self, difficulty):
        match difficulty:
            case 0:
                print("easy")
            case 1:
                print("medium")
            case 2:
                print("hard")
            case _:
                print("default")


        self.x_width = 20
        self.y_height = 20
        self.mine_min = 50
        self.mine_max = 100

        self.rows = 20
        self.cols = 20

        self.map_array_1 = [[Cell() for _ in range(self.cols)] for _ in range (self.rows)]
        self.mine_count = random.randint(50,100)



    def check_neighbors(self, x,y):
        score = 0
        score += self.local_check((x-1), (y-1))
        score += self.local_check(x, (y-1))
        score += self.local_check((x+1), (y-1))

        score += self.local_check((x-1), y)
        score += self.local_check((x+1), y)

        score += self.local_check((x-1), (y+1))
        score += self.local_check(x, (y+1))
        score += self.local_check((x+1), (y+1))

        return score
        

    def local_check(self, x,y):
        if x < 0 or x > (self.x_width -1):
            return False
        if y < 0 or y > (self.y_height -1):
            return False
        if self.map_array_1[x][y].mine == True:
            return True
        else:
            return False
        

    def fill_map(self, mine_count):
        i = 0
        while i < mine_count:
            x_random = random.randint(0,(self.x_width - 1))
            y_random = random.randint(0,(self.y_height - 1))
            if self.map_array_1[x_random][y_random].mine == False:
                self.map_array_1[x_random][y_random].mine = True
                i += 1


    def setup_maps(self):
        print("for map cell array: x ", self.x_width, " y", self.y_height)

        mine_count = random.randint(self.mine_min,self.mine_max)

        self.fill_map(mine_count)

        for j in range(self.y_height):
            for i in range(self.x_width):
                self.map_array_1[i][j].score = self.check_neighbors(i,j)


    def print_map_details(self):
        for j in range(self.y_height):
            for i in range(self.x_width):
                if self.map_array_1[i][j].mine == True:
                    print("x", end="")
                else:
                    print("-", end="")
            print(" |")

        print(" finished printing map with locations")
        print("")

        for j in range(self.y_height):
            for i in range(self.x_width):
                score = self.check_neighbors(i,j)
                self.map_array_1[i][j].score = score
                print(score, end="")
            print(" |")




    def print_map(self):
        for j in range(self.y_height):
            for i in range(self.x_width):
                if self.map_array_1[i][j].show == True:
                    print(self.map_array_1[i][j].score, end="")
                else:
                    print("-", end="")
            print(" |")



    def reveal_spread(self, x,y,counter):
        if x < 0 or x >= self.x_width:
            return
        if y < 0 or y >= self.y_height:
            return
        counter -= 1
        if counter <= 0:
            return
        if self.map_array_1[x][y].show == False:
            if self.map_array_1[x][y].mine == False:
                self.map_array_1[x][y].show = True
                self.reveal_spread(x-1,y, counter)
                self.reveal_spread(x+1,y, counter)
                self.reveal_spread(x,y-1, counter)
                self.reveal_spread(x,y+1, counter)




    def game_loop(self):
        player_lives = 2
        while(player_lives > 0):
            self.print_map()
            number_valid = False
            while number_valid == False:
                x_move = int(input("x: "))
                y_move = int(input("y: "))
                print("x is : ", x_move, "y is :", y_move)
                if x_move >= 0 and x_move < self.x_width:
                    if y_move >= 0 and y_move < self.y_height:
                        number_valid = True
            
            if self.map_array_1[x_move][y_move].mine == True:
                print("player lost")
                exit()
            else:
                #reveal_array[x_move][y_move] = True
                print("good choice")
                self.reveal_spread(x_move,y_move,4)


def main():

    input_check = False
    while input_check == False:
        user_input = int(input("choose difficulty 0 easy 1 medium 2 hard:"))
        if 0 <= user_input <= 2:
            input_check = True

    new_game = Game(user_input)

    new_game.setup_maps()

    new_game.print_map_details()

    new_game.game_loop()


main()
    

