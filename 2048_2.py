import random as rad

#><

class Board:
    def __init__(self, board_size=4, spawnsPerMove=1, gameLimit=1):

        self.board = []
        self.size = board_size

        self.active = True
        self.recursions = 2

        self.spawns = spawnsPerMove

        self.limit = self.squareNum(2, gameLimit + 10)

        print(f"\n . Game limit: {self.limit}")

        self.create_board()

        while self.active:
            self.checkWin()

            if self.active != True:
                break

            for i in range(0, self.spawns):
                self.generate()

            self.print_board()

            self.askMove()


    #INPUT AND OUTPUT
    def create_board(self):
        for i in range(self.size):
            self.board.append([0] * self.size)

    def print_board(self):
        print()
        for x in self.board:
            for y in x:
                if y == 0:
                    print(".", end="  ")
                    continue
                print(y, end="  ")
            print()
        print()

    def askMove(self):
        move = str.lower(input("Choose a move (WASD): "))

        if move == "w":
            self.compressUp(0)
        elif move == "a":
            self.compressLeft(0)
        elif move == "s":
            self.compressDown(0)
        elif move == "d":
            self.compressRight(0)
        elif move == "esc":
            self.endGame(-1)
        else:
            print("Invalid move")
            self.askMove()

    #MOVE LOGIC
    def generate(self):
        x = rad.randint(0, self.size - 1)
        y = rad.randint(0, self.size - 1)

        while self.board[x][y] != 0:
            x = rad.randint(0, self.size - 1)
            y = rad.randint(0, self.size - 1)

            if(self.checkFull() == True):
                self.endGame(0)
                break
        
        randomGen = rad.randint(1, 10)

        if(randomGen != 10):
            self.board[y][x] = 4
        else:
            self.board[y][x] = 2

    def compressRight(self, rec: 0):
        for y in range(0, self.size):
            for x in range(0, self.size - 1):
                if self.board[y][x + 1] == 0:
                    self.board[y][x + 1] = self.board[y][x]
                    self.board[y][x] = 0

                    self.mergeRight()

        #Recursiona hasta 3 veces
        if rec < self.recursions:
            rec += 1
            self.compressRight(rec)

    def compressLeft(self, rec=0):
        for y in range(0, self.size):
            for x in range(self.size - 1, 0, -1):
                if self.board[y][x - 1] == 0:
                    #a = self.board[y][x]
                    self.board[y][x - 1] = self.board[y][x]
                    self.board[y][x] = 0

                    self.mergeLeft()

        #Recursiona hasta 3 veces
        if rec < self.recursions:
            rec += 1
            self.compressLeft(rec)

    def compressDown(self, rec):
        for y in range(0, self.size - 1):
            for x in range(0, self.size):
                if self.board[y + 1][x] == 0:
                    self.board[y + 1][x] = self.board[y][x]
                    self.board[y][x] = 0

                    self.mergeDown()

        #Recursiona hasta 3 veces
        if rec < self.recursions:
            rec += 1
            self.compressDown(rec)
    
    def compressUp(self, rec):
        for y in range(self.size - 1, 0, -1):
            for x in range(0, self.size):
                if self.board[y - 1][x] == 0:
                    self.board[y - 1][x] = self.board[y][x]
                    self.board[y][x] = 0

                    self.mergeUp()

        #Recursiona hasta 3 veces
        if rec < self.recursions:
            rec += 1
            self.compressUp(rec)

    def mergeRight(self, right=0):
        for y in range(0, self.size):
            for x in range(self.size - 1, 0, -1):
                if self.board[y][x - 1] == self.board[y][x]:
                    self.board[y][x - 1] = self.board[y][x] * 2
                    self.board[y][x] = 0

    def mergeLeft(self):
        for y in range(0, self.size):
            for x in range(self.size - 1, 0, -1):
                if self.board[y][x - 1] == self.board[y][x]:
                    self.board[y][x - 1] = self.board[y][x] * 2
                    self.board[y][x] = 0

    def mergeDown(self):
        for y in range(0, self.size - 1):
            for x in range(0, self.size):
                if self.board[y + 1][x] == self.board[y][x]:
                    self.board[y + 1][x] = self.board[y][x] * 2
                    self.board[y][x] = 0

    def mergeUp(self):
        for y in range(self.size - 1, 0, -1):
            for x in range(0, self.size):
                if self.board[y - 1][x] == self.board[y][x]:
                    self.board[y - 1][x] = self.board[y][x] * 2
                    self.board[y][x] = 0

    #GAME LOGIC
    def checkFull(self):
        leftSpots = 0

        for x in range(0, self.size):
            for y in range(0, self.size):
                if(self.board[y][x] == 0):
                    leftSpots += 1

        if(leftSpots == 0):
            return True

        return False
    
    def checkWin(self):
        for x in range(0, self.size):
            for y in range(0, self.size):
                if self.board[x][y] >= self.limit:
                    self.endGame()


    def endGame(self, int=1):
        self.active = False

        if int == 0:
            print("\n . Board is full, you lose\n")
            return
        
        if int == -1:
            print("\n . Game terminated.\n")
            return

        print(f"\n . You got to {self.limit}! You win!\n")

    #LOGIC
    def squareNum(self, a, b):
        c = a

        for i in range(2, b, 1):
            a *= c

        return a

if __name__ == "__main__":
    askSize = int(input("\n - Choose board size: \n  --"))
    askSpawn = int(input("\n - Choose spawns per move: \n  --"))
    askDifficulty = int(input("\n - Choose difficulty (1-5)\n  --"))

    Board(askSize, askSpawn, askDifficulty)

    