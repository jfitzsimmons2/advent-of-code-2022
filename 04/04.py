
overlaps1 = 0
overlaps2 = 0
    
def process_set(s):
    global overlaps1
    global overlaps2
    sets = []
    for x in s:
        sets.append(x.split("-"))

    s1 = sets[0]
    s2 = sets[1]
    if (int(s1[0]) >= int(s2[0]) and int(s1[1]) <= int(s2[1])) or (int(s1[0]) <= int(s2[0]) and int(s1[1]) >= int(s2[1])):
        overlaps1 += 1

    if (int(s1[0]) <= int(s2[0]) <= int(s1[1])) or ((int(s1[0])) <= (int(s2[1])) <= (int(s1[1]))) or ((int(s2[0])) <= (int(s1[0])) <= (int(s2[1]))) or ((int(s2[0])) <= (int(s1[1])) <= (int(s2[1]))):
        overlaps2 += 1
    
    print(sets);
    print(overlaps1);
    print(overlaps2);


with open('input.txt') as f:
    lines = f.read().splitlines()
    # print(lines)
    for x in lines:
        s = x.split(",")
        process_set(s)
            
    