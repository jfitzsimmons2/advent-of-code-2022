directions = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
seen = [(0,0)]
headPos = (0,0)
tailPos = (0,0)
tails = []
headPath = [(0,0)]
    
def add_tuples(tup1, tup2):
    return tuple(map(sum, zip(tup1, tup2)))

def move_head(direction):
    global headPos
    print("adding", directions[direction])
    headPos = add_tuples(headPos, directions[direction]);
    headPath.append(headPos)
    print("Moved head to", headPos);

def move_tail(direction):
    global tailPos
    tailPos = add_tuples(tailPos, directions[direction]);
    
def is_touching():
    global headPos
    global tailPos
    hx, hy = headPos
    tx, ty = tailPos
    return abs(hx-tx) <= 1 and abs(hy-ty) <= 1;

def handle_tail():
    global tailPos
    hx, hy = headPos
    tx, ty = tailPos

    # If the head is ever two steps directly up, down, left, or right from the tail, 
    # the tail must also move one step in that direction so it remains close enough:
    print(is_touching())
    if (is_touching()):
        return
    
    if (hx-tx == 0 or hy-ty == 0):
        print(hx,"-",tx)
        print(hy,"-",ty)
        if (hx - tx == 2):
            move_tail("R")

        elif (hx - tx == -2):
            move_tail("L")

        elif (hy - ty == 2):
            move_tail("U")

        elif (hy - ty == -2):
            move_tail("D")
        
    # otherwise, if the head and tail aren't touching and aren't in the same row or column, 
    # the tail always moves one step diagonally to keep up:
    else:
        if (hx - tx == -2):
            move_tail("L")
            move_tail("U") if (hy - ty > 0) else move_tail("D")
        if (hy - ty == 2):
            move_tail("U")
            move_tail("R") if (hx - tx > 0) else move_tail("L")
        if (hx - tx == 2):
            move_tail("R")
            move_tail("U") if (hy - ty > 0) else move_tail("D")
        if (hy - ty == -2):
            move_tail("D")
            move_tail("R") if (hx - tx > 0) else move_tail("L")
               
    seen.append(tailPos)

def do_the_thing(direction, amount):
    for _ in range(amount):
        move_head(direction)
        handle_tail()

with open("input.txt", "r") as f:
    for line in f.read().splitlines():
        direction, amount = line.split()
        amount = int(amount)
        print("\n")
        print(line)
        do_the_thing(direction, amount);
        
    print(seen);
    print(len(list(set(seen))))
