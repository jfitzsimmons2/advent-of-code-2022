import re

stacks = [];

def create_stacks(num):
    global stacks;
    for i in range(num):
        stacks.append([])

# No hardcoded stacks for this guy
def parse_stack(line):
    global stacks

    pattern = "\[\S\]"
    # look for crates
    if re.search(pattern, line) is not None:
        match = re.finditer(pattern, line)
        
        for m in match:
            stackIndex = int(m.span()[0] / 4)
            letter = m.string[m.span()[0]:m.span()[1]].strip("[]")
            stacks[stackIndex].insert(0,letter)
        return True
    else: 
        return False


with open('input.txt') as f:
    lines = f.read().splitlines()

    # First pass, get number of stacks
    for x in lines:
        line = x.split();
        print(line[0])
        if (line[0] == "1"):
            print("numbers")
            create_stacks(int(line[len(line)-1]))
            break

    # second pass
    for x in lines:
        if (parse_stack(x)):
            continue
            
        elif (len(x.split()) == 6):
            move = int(x.split()[1]);
            _from = int(x.split()[3]) - 1;
            to = int(x.split()[5]) - 1;

            moving = stacks[_from][-move:]

            #part1
            #moving.reverse()
            
            stacks[_from] = stacks[_from][: len(stacks[_from]) - move]
            stacks[to] = stacks[to] + moving
            
    result = [] 

    for i,stack in enumerate(stacks):
        print(i, stack);
        result.append(stack.pop())
    
    print("".join(result))