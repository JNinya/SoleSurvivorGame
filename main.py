#import modules
import os
import fh
import parseScene

#core gameloop
def gameloop(scene):
    #clear the screen
    os.system('cls')

    #parsing & printing the text (done with the parseScenes module)
    print(parseScene.description(scene))

    #interpret user input. Selects destination scene
    choice = str(input()).upper()
    scene = str(scene)
    pointerMap = parseScene.where(scene)
    if choice in pointerMap:
        destinationScene = parseScene.where(scene)[choice]
    else:
        gameloop(scene)

    #open new scene that the user chose
    gameloop(destinationScene)

#start the game
os.system('color a')
os.system('cls')
gameloop(0)

# end by gabe