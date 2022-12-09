from functools import reduce


visible = 0
global_score=[]

def check_visibility(x,y):
    global visible
    
    col = check_column(x,y)
    row = check_row(x,y)
    if (is_edge(x,y) or col or row ):
        visible += 1;
        
def is_edge(x,y):
    edgeFlag = y==0 or y==len(matrix)-1 or x==0 or x == len(matrix[0])-1
    return edgeFlag

def check_column(x,y):
    val = int(matrix[y][x])
    col = list(map(int, column(x)))
    
    topArray = col[0:y]
    bottomArray = col[y+1:len(matrix[0])]
    
    get_score(val,topArray,"TOP");
    get_score(val,bottomArray,"BOTTOM");

    if (is_edge(x,y)):
        return True
    else:
        return max(topArray) < val or val > max(bottomArray)

def check_row(x,y):
    val=int(matrix[y][x])
    row = list(map(int, matrix[y]));
    leftArray = row[0:x]
    rightArray = row[x+1:len(matrix[0])]

    get_score(val, leftArray, "LEFT");
    get_score(val, rightArray, "RIGHT");
 
    if (is_edge(x,y)):
        return True
    else:
        return max(leftArray) < val or val > max(rightArray)

def column(i):
    return [row[i] for row in matrix]

def get_score(val, array, direction):
    index = 0;

    if (len(array) == 0):
        global_score.append(0)
        return

    if (direction == "LEFT" or direction == "TOP"):
        array.reverse();

    while index < len(array):
        if (array[index] >= val or index == len(array) - 1):
            score = index + 1
            global_score.append(score);
            break;
        index += 1

with open("input.txt", "r") as f:
    matrix = []
    for line in f.read().splitlines():
        array = [x for x in line]
        matrix.append(array);

    max_score = 0;
    for i,row in enumerate(matrix):
        for j,cell in enumerate(row):
            check_visibility(j,i)
            s = 0
            if (len(global_score) == 4):
                s = reduce((lambda x, y: x * y), global_score)
            if (s>max_score):
                max_score = s
            global_score = []

    print("visible",visible)
    print("max score",max_score)
