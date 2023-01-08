'''
Author: Josh Bellingham
Version: 2023-01-06
Description: Coding an azul clone in Python partly for fun and 
partly so I can play the game on my TV and 
partly so I can sell it to the game company and make a million dollars...
'''
import random

#Make a class for tiles, and then make 100 tiles with 5 different colours

class Tile:
    def __init__(self, color, idn):
        self.color = color
        self.idn = idn
    
    def __repr__(self):
        return f"{self.color}({self.idn})"

colors = ["red", "blue", "yellow", "white", "black"]

#Make a 'sac' that store all the inital game tiles

sac = []

#start game by putting 20 of each color tile in the sac
for x in range(1, 21):
    tilex = Tile("red", x)
    sac.append(tilex)   
for x in range(1, 21):
    tilex = Tile("blue", x)
    sac.append(tilex)
for x in range(1, 21):
    tilex = Tile("yellow", x)
    sac.append(tilex)
for x in range(1, 21):
    tilex = Tile("white", x)
    sac.append(tilex) 
for x in range(1, 21):
    tilex = Tile("black", x)
    sac.append(tilex)

#Make a 'bucket' that store all the played game tiles

#Make 'mats', which take the number of players and assign the appropriate number of playable spaces
selecting = True
while selecting == True:
    players = int(input("How many players do you have?\n"))

    try:
        if players > 2:
            print("Unfortunately, you need at least 2 players to play Azul. Go find some friends!")
        if players == 2:
            selecting = False
            print("Setting out 5 mats...")
            mat1 = []
            mat2 = []
            mat3 = []
            mat4 = []
            mat5 = []
        if players == 3:
            selecting = False
            print("Setting out 7 mats...")
            mat1 = []
            mat2 = []
            mat3 = []
            mat4 = []
            mat5 = []
            mat6 = []
            mat7 = []
        if players == 4:
            selecting = False
            print("Setting out 9 mats...")
            mat1 = []
            mat2 = []
            mat3 = []
            mat4 = []
            mat5 = []
            mat6 = []
            mat7 = []
            mat8 = []
            mat9 = []
        if players > 4:
            print("Sorry, Azul only supports up to 4 players at a time. You'll just have to take turns!")
        else:
            raise TypeError("Please enter an interger between 2 and 4.")
    except TypeError:
        print("")
    
begin = input("When you are ready to begin the game, type begin!")
if begin == "begin":
    if players == 2:
        for i in range(4):
            choice = random.choice(sac)
            mat1.append(choice)
            sac.remove(choice)
        for i in range(4):
            choice = random.choice(sac)
            mat2.append(choice)
            sac.remove(choice)
        for i in range(4):
            choice = random.choice(sac)
            mat3.append(choice)
            sac.remove(choice)
        for i in range(4):
            choice = random.choice(sac)
            mat4.append(choice)
            sac.remove(choice)
        for i in range(4):
            choice = random.choice(sac)
            mat5.append(choice)
            sac.remove(choice)
        print("Mat 1: ", mat1, "\nMat 2: ", mat2, "\nMat 3: ", mat3, "\nMat 4: ", mat4, "\nMat 5: ", mat5)
    if players == 3:
        for i in range(4):
            choice = random.choice(sac)
            mat1.append(choice)
            sac.remove(choice)
        for i in range(4):
            choice = random.choice(sac)
            mat2.append(choice)
            sac.remove(choice)
        for i in range(4):
            choice = random.choice(sac)
            mat3.append(choice)
            sac.remove(choice)
        for i in range(4):
            choice = random.choice(sac)
            mat4.append(choice)
            sac.remove(choice)
        for i in range(4):
            choice = random.choice(sac)
            mat5.append(choice)
            sac.remove(choice)
        for i in range(4):
            choice = random.choice(sac)
            mat6.append(choice)
            sac.remove(choice)
        for i in range(4):
            choice = random.choice(sac)
            mat7.append(choice)
            sac.remove(choice)
        print("Mat 1: ", mat1, "\nMat 2: ", mat2, "\nMat 3: ", mat3, "\nMat 4: ", mat4, "\nMat 5: ", mat5,
              "\nMat 6: ", mat6, "\nMat 7: ", mat7)
    if players == 4:
        for i in range(4):
            choice = random.choice(sac)
            mat1.append(choice)
            sac.remove(choice)
        for i in range(4):
            choice = random.choice(sac)
            mat2.append(choice)
            sac.remove(choice)
        for i in range(4):
            choice = random.choice(sac)
            mat3.append(choice)
            sac.remove(choice)
        for i in range(4):
            choice = random.choice(sac)
            mat4.append(choice)
            sac.remove(choice)
        for i in range(4):
            choice = random.choice(sac)
            mat5.append(choice)
            sac.remove(choice)
        for i in range(4):
            choice = random.choice(sac)
            mat6.append(choice)
            sac.remove(choice)
        for i in range(4):
            choice = random.choice(sac)
            mat7.append(choice)
            sac.remove(choice)
        for i in range(4):
            choice = random.choice(sac)
            mat8.append(choice)
            sac.remove(choice)
        for i in range(4):
            choice = random.choice(sac)
            mat9.append(choice)
            sac.remove(choice)
        print("Mat 1: ", mat1, "\nMat 2: ", mat2, "\nMat 3: ", mat3, "\nMat 4: ", mat4, "\nMat 5: ", mat5,
              "\nMat 6: ", mat6, "\nMat 7: ", mat7, "\nMat 8: ", mat8, "\nMat 9: ", mat9)
else:
    print("Please type 'begin' to begin the game")

#Make a function that fills the mats with 4 tiles each,, first from the sac, then from the bucket

#Make the game board

#Make the middle 'table' section to store tiles

#Define a function for players to take a tile from the mat and have the remain tiles go to the table

#Define a function for players to move tiles around on their boards

#Define function for 'one tile' that can be taken from the middle and only placed in a negative slot on the game board

#Once all the tiles are gone from the mats and table, have the game score based on Azul rules and store that info to a player score variable

#Once one of the end conditions are met, either a row across, or running out of tiles, have the game add point to player (+10 for diagonals, +7 for verticals, +2 for horizontals)