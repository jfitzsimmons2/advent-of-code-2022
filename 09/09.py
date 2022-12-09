movesKey = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

with open("input-example.txt", "r") as f:
    for line in f.read().splitlines():
        direction, amount = line.split()
        
