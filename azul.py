'''
Author: Josh Bellingham
Version: 2023-01-06
Description: Coding an azul clone in Python partly for fun and 
partly so I can play the game on my TV and 
partly so I can sell it to the game company and make a million dollars...
'''

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

print(sac)

#Make a 'bucket' that store all the played game tiles

#Make 'mats', which take the number of players and assign the appropriate number of playable spaces

mat = [] #needs to have a limit of 4 tiles

#Make a function that fills the mats with 4 tiles each,, first from the sac, then from the bucket

#Make the game board

#Make the middle 'table' section to store tiles

#Define a function for players to take a tile from the mat and have the remain tiles go to the table

#Define a function for players to move tiles around on their boards

#Define function for 'one tile' that can be taken from the middle and only placed in a negative slot on the game board

#Once all the tiles are gone from the mats and table, have the game score based on Azul rules and store that info to a player score variable

#Once one of the end conditions are met, either a row across, or running out of tiles, have the game add point to player (+10 for diagonals, +7 for verticals, +2 for horizontals)