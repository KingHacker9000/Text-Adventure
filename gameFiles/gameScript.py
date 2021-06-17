import sys
from time import sleep
sys.path.append("..")
import gameEngine
from gameClasses import *
from gameEngine import *

# Variables
frameCount = 0

width = 51
height = 51

myCam = camera(width/2-1, height/2-1)
myMap = makeMap(width, height, myCam)

#------------
# Game rules
#------------

class Game:

    def __init__(self, engine, cam):

        self.frameCount = 0
        self.engine = engine
        self.camera = cam

    # Runs Before First Frame of Game
    def awake(self):

        print("Welcome to Your 0D Text Adventure")
        input("\nClick Enter to Start Game:")

        sleep(1)
        print("\n\nbEeeEeeeEEEeepp!!! beeEEeEeeeEp! BeeeEEeeeEEEEeeep!!\n")
        sleep(1.2)
        print("___________\n| 7 : 15 |\n__________")
        print("（；¬＿¬)\n")
        sleep(1)
        print("You: Oh NO! I overSlept again!!")
        sleep(1)
        print("You: I have to reach before 7:40, before Computer class starts ")
        print("( #`⌂´)/\n")
        sleep(1.7)

        print("******************************")
        print("       Rules of the Game      ")
        print("  1)type l to go left \n  2)type r to go right")
        print("******************************")
        sleep(3)

        print("\n\nYou Live in Sharjah, You'll need to get to Al Safa")
        sleep(1)
        case1 = input("Will you go Right to Deira or left to Al Aweer Exit?:")

        while case1 != 'r' and case1 != 'l':
            print("r for right\nl for left")
            case1 = input("Will you go Right to Deira or left to Al Aweer Exit?:")
        if case1 != "r":
            sleep(1)
            print("You make your way onto Al Aweer Exit\n")
            sleep(1.5)
            print("You wandered off the path to school and you were never found again\n\n")
            sleep(3)
            print("================================")
            print("||          Game Over         ||")
            print("================================")
            exit()

        sleep(1)
        print("\n\nYou make your way onto Deira \nYou reach yet annother fork on the road to school")
        case2 = input("Will you go Right to BurDubai or left to Karama?:")

        while case2 != 'r' and case2 != 'l':
            print("r for right\nl for left")
            case2 = input("Will you go Right to BurDubai or left to Karama?:")
        if case2 != "r":
            sleep(1)
            print("You make your way onto Karama")
            sleep(1.5)
            print("You wandered off the path to school and you were found years later, but by that time, you had become mental, you spoke of an empty place where all there was were rocks and your school in the distance, but u cudnt reach your school because you made the wrong choices\n\n")
            sleep(3)
            print("================================")
            print("||          Game Over         ||")
            print("================================")
            quit()

        sleep(1)
        print("\n\nYou make your way onto BurDubai \nYou reach the last fork on the road to school")
        case3 = input("Will you go Right to Jumeirah Beach or Left to looɥɔS ǝʇɐʌıɹԀ SSſ:")

        while case3 != 'r' and case3 != 'l':
            print("r for right\nl for left")
            case3 = input("Will you go Right to BurDubai or left to Karama?:")
        if case3 != "l":
            sleep(1)
            print("You make your way onto ʇıdɐʌɐl ɥɐɹıǝɯnſ")
            sleep(1.5)
            print("You wandered off the path to school and you were found years later, but it was only your burnt body\n\n")
            sleep(3)
            print("================================")
            print("||          Game Over         ||")
            print("================================")
            quit()

        sleep(2)
        print("\n\nYou make your way onto looɥɔS ǝʇɐʌıɹԀ SSſ")
        sleep(2.5)
        print("Suddenly The Ground Shakes")
        sleep(2)
        print("You feel your world collapse in itself")
        sleep(2)
        print("You see a strange thing appear")
        sleep(0.2)
        print("###################################")
        sleep(2)
        print("What could it be, can you touch it?")
        print("###################################\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        sleep(2)
        print("###################################")
        print("Welcome to Your 1D Text Adventure")
        print("\nClick Enter to Start Game: ")
        input("###################################")

        sleep(2)
        print("Well thats wierd...Didnt the game already start?")
        print("###################################")
        sleep(2)
        print("Suddenly the ground start trembling again")
        print("###################################")
        sleep(2)
        print("You begin paniking")
        print("###################################")
        print("you feel an immense streching sensation")
        print("Aaahh")
        print("h\nhhh\nhhh\nhh\nhh\nhh\nh\nh\nh\nh\nh\nh")
        sleep(2)
        print("You:...ughhh what happened?")
        sleep(2)
        print("You: Where am I? I need to reach School Quick!")
        print("You slowly open your eyes\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        sleep(2)

        print("###################################")
        print("#Welcome to Your 2D Text Adventure#")
        print("#                                 #")
        print("#Click Enter to Start Game:       #")
        input("###################################")
        sleep(3)

        
        

    # Runs After First Frame of Game
    def start(self):
        self.frameCount += 1

        print("\n\n")
        sleep(3)
        print("****************************************************************")
        print("*                      Rules of the Game                       *")
        print("*  1)to move put <direction> <space> <number of steps to move> *")
        print("*  2)l = left; r = right; u = up; d = down                     *")
        print("*  Ex: To move 5 steps right: r 5                              *")
        print("*                                                              *")
        print("*  Objective: Reach School on time, you are i                  *")
        print("*  Hint: use map to print out the map                          *")
        print("****************************************************************")
        sleep(3)


    # Runs before displaying a frame
    def update(self):
        self.frameCount += 1

        if self.frameCount > 10:
            print("You wandered off the path to school and you never found a way to school")
            sleep(2)
            print("You were stuck in this upside down universe")
            sleep(3)
            print("================================")
            print("||          Game Over         ||")
            print("================================")
            quit()
        
        if ((myCam.pos.x - myMap.desX)**2)**0.5 <= self.camera.width-5 and ((myCam.pos.y - myMap.desY)**2)**0.5 <= self.camera.height-3:
            self.engine.gameQuit()
        
        move = input("Move:\t").split(" ")
        
        if move[0] == "u":
            myCam.move(myMap, 0, -int(move[1]))

        elif move[0] == "d":
            myCam.move(myMap, 0, int(move[1]))

        elif move[0] == "r":
            myCam.move(myMap, int(move[1]), 0)

        elif move[0] == "l":
            myCam.move(myMap, -int(move[1]), 0)

        elif move[0] == "map":
            myMap.printWorld()
            

    # Runs after displaying a frame
    def lateUpdate(self):
        pass

#------------
# Start Game
#------------
gameEngine = Engine()
myGame = Game(gameEngine, myCam)
gameEngine.play(myCam, myMap, myGame)
