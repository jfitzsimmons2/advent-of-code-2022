import sys

directions = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
seen = [(0,0)]
rope = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
tailIndex = 0
    
def debug(a=None,b=None,c=None,d=None):
    if (sys.argv[1] == "input.txt"):
        return

    if (b==None):
        print(a);
        return
    if (c==None):
        print(a,b);
        return
    if (d==None):
        print(a,b,c);
        return
    if (a != None and b != None and c != None and d != None):
        print(a,b,c,d)

def add_tuples(tup1, tup2):
    return tuple(map(sum, zip(tup1, tup2)))

def move_tail(direction):
    global tailIndex
    global directions
    global rope
    rope[tailIndex] = add_tuples(rope[tailIndex], directions[direction]);

def move_head(direction):
    global rope
    global directions
    #debug("adding", directions[direction])
    rope[0] = add_tuples(rope[0], directions[direction])
    #debug("Moved head to", rope[0])

def is_touching():
    global tailIndex
    global rope
    
    hx, hy = rope[tailIndex-1];
    tx, ty = rope[tailIndex]
    return abs(hx-tx) <= 1 and abs(hy-ty) <= 1;

def handle_tail():
    global rope
    global tailIndex

    # debug("\nbefore handle_tail", tailIndex)
    # debug("Tail",tailIndex-1, rope[tailIndex-1])
    # debug("Tail",tailIndex , rope[tailIndex])
    
    hx, hy = rope[tailIndex-1];
    tx, ty = rope[tailIndex]

    # If the head is ever two steps directly up, down, left, or right from the tail, 
    # the tail must also move one step in that direction so it remains close enough:
    if (is_touching()):
        # debug("touching, no action needed")
        return

    if (hx - tx == 0 or hy - ty == 0):
        # debug(hx,"-",tx)
        # debug(hy,"-",ty)
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
        if (hx - tx == 2 and hy - ty == 2):
            move_tail("R")
            move_tail("U")
        elif (hx-tx == 2 and hy-ty == -2):
            move_tail("R")
            move_tail("D")
        elif (hx-tx == -2 and hy-ty == 2):
            move_tail("L")
            move_tail("U")
        elif (hx - tx == -2 and hy - ty == -2):
            move_tail("L")
            move_tail("D")
        else:
            if (hx - tx == -2):
                move_tail("L")
                move_tail("U") if (hy - ty > 0) else move_tail("D")
            if (hx - tx == 2):
                move_tail("R")
                move_tail("U") if (hy - ty > 0) else move_tail("D")
            if (hy - ty == 2):
                move_tail("U")
                move_tail("R") if (hx - tx > 0) else move_tail("L")
            if (hy - ty == -2):
                move_tail("D")
                move_tail("R") if (hx - tx > 0) else move_tail("L")
            
    # debug("after handle_tail", tailIndex)
    # debug("Tail",tailIndex-1, rope[tailIndex-1])
    # debug("Tail",tailIndex , rope[tailIndex])

    seen.append(rope[9])

def do_the_thing(direction, amount):
    global tailIndex
    for _ in range(amount):
        move_head(direction)
        tailIndex = 1
        debug(tailIndex)
        while tailIndex < 10:
            handle_tail()
            tailIndex += 1
        debug('\n')

with open(sys.argv[1], "r") as f:
    for line in f.read().splitlines():
        direction, amount = line.split()
        amount = int(amount)
        
        debug(line)
        do_the_thing(direction, amount);
        debug(rope)
        
    print(seen);
    print(len(list(set(seen))))
