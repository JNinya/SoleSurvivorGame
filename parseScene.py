"""
Functions:

description(sceneNumber)

where(inputNumber)

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

#take in a an input number and give out a new scene number based on the pointers included in the scene file
def where(inputNumber):
    #rawText gets the whole file in the raw
    rawText = fh.read("scenes/" + str(inputNumber))

    #split based on the ';' operator
    splitText = rawText.split(";\n")

    #get just the pointers from the selected scene file
    pointers = splitText[1]

    return(pointers)