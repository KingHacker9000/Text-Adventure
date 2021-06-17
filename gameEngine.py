import sys
sys.path.append(".")
from gameClasses import *



class Engine:

    def __init__(self):
        self.gameOver = False

    # Functions
    def loadLevel(self, lvlMap):
        lvlMap.load2DMap()
        lvlMap.updateMap()

    def display(self, cam, lvlMap):

        print("#" * (cam.width + 2))
        for i in range(1, cam.height-1):
            print("#", end="")
            
            for j in range(cam.width):

                x = int(cam.pos.x - (cam.width/2)) + j
                y = int(cam.pos.y - (cam.height/2)) + i
                
                print(lvlMap.position(x, y), end="")

            print("#")
            
        print("#" * (cam.width + 2))

    def start_(self):
        pass

    def awake_(self):
        pass

    def update_(self):
        print("Empty")

    def lateUpdate_(self):
        return False

    def gameQuit(self):
        self.gameOver = True

    # Start Game

    def play(self, camera, levelMap, game):

        self.loadLevel(levelMap)
        
        game.awake()
        if self.gameOver:
            return
        self.display(camera, levelMap)
        game.start()

        while True:
            game.update()
            levelMap.updateMap()
            self.display(camera, levelMap)
            if self.gameOver:
                break
            game.lateUpdate()

        print("You found Your way To School!!")
            

