# dict of dirs    
dirDict = {'/':0}
cwd = ['/']
with open("input.txt", "r") as f:
    for line in f.read().splitlines():
        parts = line.split(" ")
        # print(parts);
        #command
        if parts[0] == '$':
            if parts[1] == 'cd':
                if parts[2] == '..':
                    cwd.pop()
                elif parts[2] == '/':
                    cwd = ['/']
                else:
                    cwd.append(parts[2])
        #make dir
        elif parts[0] == 'dir':
            #print(cwd)
            dir = "".join(cwd) + parts[1]
            #print(dir);
            dirDict[dir] = 0
        #add file sizes to dict
        else:
            dir = "".join(cwd)
            dirDict[dir] += int(parts[0])
            for i in range(1, len(cwd)):
                dirDict["".join(cwd[:-i])] += int(parts[0])

#print("\n\n", dirDict)

def get_sum():
    acc = 0;
    for v in dirDict.values():
        if (v <= 100000):
            acc += v
    return acc

def part_2():
    totes = [];
    for v in dirDict.values():
        if (v >= dirDict["/"] - 40000000):
            totes.append(v)
    return min(totes)


print("part 1", get_sum())
print("part 2", part_2())