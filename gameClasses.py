import random
from time import sleep

#classes
class pos:

    def __init__(self, x, y):

        self.x = x
        self.y = y

class player:

    def __init__(self, x, y):

        position = pos(x, y)
        self.position = position

class object:

    def __init__(self, x, y):

        position = pos(x, y)
        self.position = position
        

class makeMap:

    def __init__(self, width, height, player):

        self.width = width
        self.height = height
        self.board = []
        self.player = player
        self
        self.initializeBoard()
        self.destination = [["/", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "\\" ],
                            ["|", " ", "J", "S", "S", " ", "P", "R", "I", "V", "A", "T", "E", " ", "|"],
                            ["|", " ", " ", " ", "S", "C", "H", "O", "O", "L", " ", " ", " ", " ", "|"],
                            ["|", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "|" ]
                             ]

        self.desX = random.randint(0, self.width-len(self.destination[0]))
        self.desY = random.randint(0, self.height-len(self.destination))

        while ((player.pos.x - self.desX)**2)**0.5 <= player.width-5 and ((player.pos.y - self.desY)**2)**0.5 <= player.height-3:
            self.desX = random.randint(0, self.width-len(self.destination[0]))
            self.desY = random.randint(0, self.height-len(self.destination))

    def position(self, x, y):
        return self.board[y][x]

    def initializeBoard(self):
        
        for y in range(self.height):
            row = []

            for x in range(self.width):
                row.append(" ")

            self.board.append(row)


    def updateMap(self):
        self.board[int(self.player.pos.y)][int(self.player.pos.x)] = "i"
        self.board[int(self.player.previousPos.y)][int(self.player.previousPos.x)] = "_"

        

    def load2DMap(self):

        for y in range(self.height):
            for x in range(self.width):
                self.board[y][x] = "_"

                if random.randint(0,20) < 2:
                    self.board[y][x] = "O"

        for y in range(len(self.destination)):
            for x in range(len(self.destination[0])):
                self.board[self.desY+y][self.desX+x] = self.destination[y][x]

    def printWorld(self):

        for y in range(self.height):
            for x in range(self.width):
                print(self.position(x, y), end="")
            print("", end="\n")

                


class camera:

    def __init__(self, x, y, width=27, height=12):

        position = pos(x, y)
        self.pos = position
        self.previousPos = pos(0, 0)
        
        self.width = width
        self.height = height

    def move(self,myMap, x, y):

        self.previousPos.x = self.pos.x
        self.previousPos.y = self.pos.y

        self.pos.x += x
        self.pos.y += y

        if myMap.position(int(self.pos.x), int(self.pos.y)) == "O":
            print("You fell over a Rock in the underWorld")
            sleep(2)
            print("You were not able to recover and it led to ur untimely demise")
            sleep(3)
            print("================================")
            print("||          Game Over         ||")
            print("================================")
            quit()

        
        
