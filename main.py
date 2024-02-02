#import modules
import os
import fh
import parseScene

#variables
currentScene = 0

#core gameloop
def gameloop():
    #clear the screen
    os.system('cls')

    #parsing & printing the text (done with the parseScenes module)
    print(parseScene.description(currentScene))
    #print(parseScene.where(currentScene))

    choice = input()
    gameloop()

#start the game
os.system('color a')
os.system('cls')
gameloop()

# end by gabe