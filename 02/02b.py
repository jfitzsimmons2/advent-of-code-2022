# A || X = rock
# B || Y = paper
# C || Z = scissors

# Points awarded:
# - 1 for Rock
# - 2 for Paper
# - 3 for Scissors
#  X Y Z
# A
# B
# C

# outcome of the round 
# - 0 if you lost
# - 3 if the round was a draw
# - and 6 if you won.
from enum import Enum

matrix = [["Y","Z","X"],["X","Y","Z"],["Z","X","Y"]]


winNum = {
    -1: "LOST",
    0: "DRAW",
    1: "WON"
}

letterIndexes = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2
}

letterPts = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

outcomePts = {
    -1: 0,
    0: 3,
    1: 6
}

def get_outcome_points(letter): 
    if(letter == "X"):
        print("Expected loss, 0 points")
        return 0
    if(letter == "Y"):
        print("Expected draw, 3 points")
        return 3
    if(letter=="Z"):
        print("Expected win, 6 points")
        return 6


def get_letter_points( letter ):
   return letterPts[letter]

def get_my_play_points( opponent_letter, exp_outcome):
    print("picked ___ for this many points:")
    print(matrix[letterIndexes[opponent_letter]].index(exp_outcome)+1)
    return matrix[letterIndexes[opponent_letter]].index(exp_outcome) + 1

with open('input.txt', 'r') as f:
    line = f.readline()
    total = 0;
    match = line.strip().split(' ')
    print(match)

    
    # get points of outcome for match 1
    points = get_outcome_points(match[1])
    

    # figure out my play and get points
    points += get_my_play_points(match[0], match[1])
    total += points

    while line:
        line = f.readline()
        if (line != ''):
            match = line.strip().split(' ')
            print(match)

    
            # get points of outcome for match 1
            points = get_outcome_points(match[1])
            

            # figure out my play and get points
            points += get_my_play_points(match[0], match[1])
            total += points
    
    print("Total points")
    print(total)
        