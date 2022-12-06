from collections import Counter


def find_dup_char(input):
    print("Checking", input)
    WC = Counter(input)
    res = False
    for letter, count in WC.items():
        print(letter, count)
        if (count > 1):
            res = True
    return res;

with open('input.txt') as f:
    lines = f.read().splitlines()

    # First pass, get number of stacks
    buffer = ""
    for line in lines:
        print(line)
        for i,letter in enumerate(line):
            print(i)
            #part 1
            # end = i + 4
            end = i + 14
            buff = line[i:end]
            print(buff)
            if (find_dup_char(buff)):
                continue;
            else:
                print(end);
                break;
                