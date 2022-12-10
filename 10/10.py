import sys
import numpy as np

print(sys.argv)
x = 1
cycle = 0
log = [1]

# def cycle():

def execute(cmd, num = 0):
    global cycle
    global x
    if (cmd=="addx"):
        log.append(x)
        cycle += 2;
        x += int(num)
        log.append(x)
    else:
        cycle += 1;
        log.append(x)

def get_cycle(index):
    return log[index]

def get_signal_strength(index):
    print(index, "*", log[index-1])
    return log[index-1] * index

with open(sys.argv[1], "r") as f:
    for i,line in enumerate(f.read().splitlines()):
        parts = line.split()        
        num = parts[1] if (len(parts)>1) else 0

        execute(parts[0], num)
        
        
print(get_cycle(20))
print(log[215:220])
interesting_signals = [20,60,100,140,180,220]
total = []
for i in interesting_signals:
    total.append(get_signal_strength(i))
print(len(log))
print(sum(total))

def print_pixel(index, x):
    index = index % 40;
    if (index == 0):
        print('\n', end="")
    if (x==index or x == index+1 or x== index-1):
        print("#", end="")
    else:
        print(".", end="")


sprite_pos = 2
render_result = list()

for index,x in enumerate(log):
    print_pixel(index, x)
# print(log[240])