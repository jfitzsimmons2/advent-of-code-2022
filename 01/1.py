with open('1-input.txt', 'r') as f:

    line = f.readline()
    accumulator = int(line)
    totals = []
    while line:
        line = f.readline()
        if (line == "\n"):
            totals.append(accumulator)
            accumulator = 0
        elif (line == ""):
            totals.append(accumulator)
            totals.sort()
            last3 = totals[-3:]
            print(sum(last3))
        else:
            accumulator += int(line)