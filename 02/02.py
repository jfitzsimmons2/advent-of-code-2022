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

matrix = [[0,-1,1],[1,0,-1],[-1,1,0]]

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


def get_outcome(arg1, arg2):
    return matrix[letterIndexes[arg1]][letterIndexes[arg2]]

def get_letter_points( letter ):
   return letterPts[letter]

def get_outcome_points( letter ):
   return outcomePts[letter]

with open('input.txt', 'r') as f:
    line = f.readline()
    total = 0;
    match = line.strip().split(' ')
    print(match)
    outcome = get_outcome(match[1], match[0])

    print(get_outcome(match[0], match[1]))
    points = get_outcome_points(outcome)
    points += get_letter_points(match[1])
    total += points

    while line:
        line = f.readline()
        if (line != ''):
            match = line.strip().split(' ')
            outcome = get_outcome(match[1], match[0])
            print("\n")
            print(match)
            print(winNum[outcome] + " for the " + str(get_outcome_points(outcome)) + " + " + str(get_letter_points(match[1])) + " for choosing")
            points = get_outcome_points(outcome)
            points += get_letter_points(match[1])
            print(points)
            total += points
    
    print("Total points")
    print(total)
        