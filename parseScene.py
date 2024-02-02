"""
Functions:

description(sceneNumber)

where(inputNumber, option)

"""

import fh

#get description text from the selected scene file
def description(sceneNumber):
    #rawText gets the whole file in the raw
    rawText = fh.read("scenes/" + str(sceneNumber))

    #split based on the ';' operator
    splitText = rawText.split(";\n")
    
    #return just the description (before the ; operator)
    return splitText[0]

# take in a an input number and give out a new scene number based on the pointers included in the scene file
# sceneId -> id of scene file
# option  -> option selected
# returns a map of pointers with string indices and int values
def where(sceneId):
    # rawText gets the whole file in the raw
    rawText = fh.read("scenes/" + str(sceneId))

    # split based on the ';' operator
    splitText = rawText.split(";\n")

    # read pointers into map
    pointers = splitText[1].splitlines()
    pointer_map = {}
    for pointer in pointers:
        pointer = pointer.split(">")
        pointer_map[pointer[0]] = int(pointer[1])

    return(pointer_map)

# DEBUG
print(where(0))