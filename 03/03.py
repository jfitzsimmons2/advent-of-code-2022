dupes = []

def find_dupes(first, second, third=None):
    if (third==None):
        dupes.append(list(set(first).intersection(second))[0])
    else:
        dupes.append(list(set(first).intersection(second).intersection(third))[0])

def split_rucksack(l):
    first, second = l[:len(l)//2], l[len(l)//2:]
    return [first, second]

def letter_value(l):
    return ord(l) - 38 if (ord(l) - 96 < 0) else ord(l) - 96;

def process_rucksack(string):
    first, second = split_rucksack(string)
    find_dupes(first, second)

def answer1():
    print(dupes)
    print(sum(list(map(letter_value, dupes))))

# part 1
# with open('input-example.txt', 'r') as f:
#     line = f.readline()
#     process_rucksack(line)
#     while line:
#         line = f.readline()
#         if (line != ''):
#             process_rucksack(line)

def process_cohort():
    find_dupes(cohort[0], cohort[1], cohort[2])
    find_dupes(cohort[3], cohort[4], cohort[5])
    print(cohort)
    return cohort

cohort = []

with open('input.txt') as f:
    lines = f.read().splitlines()
    for i, x in enumerate(lines):
        if (i % 6 == 0):
            cohort.clear()

        cohort.append(x)
        print(i % 3);
        print(i % 6); #new compare
        if(i % 6 == 5):
            process_cohort();


answer1()