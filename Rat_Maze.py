size = 6
maze = [
    [0,1,0,1,1,0],
    [0,0,0,0,0,0],
    [1,0,1,0,1,0],
    [0,0,1,0,0,1],
    [1,0,0,1,0,1],
    [0,0,0,0,0,0]
    ]
sol = [[0]*size for i in range(size)]

count = 0
def solveMaze(r, c):
    global count
    count+=1
    if (r == size - 1) and (c == size - 1):
        sol[r][c] = 1;
        return True;

    if (r >= 0) and (c >= 0) and (r < size) and (c < size) and (sol[r][c] == 0) and (maze[r][c] == 0):
        sol[r][c] = 1
        for d in sol:
            print(d)
        print("-----------------------", count)
        # Moving Down
        if solveMaze(r + 1, c):
           return True
        # Moving Right
        if solveMaze(r, c + 1):
           return True
        # Moving Up
        if solveMaze(r - 1, c):
           return True
        # Moving  Left
        if solveMaze(r, c - 1):
           return True
        # Backtracking
        sol[r][c] == 0;
        for d in sol:
            print(d)
        print("-----------------------", count)
        return False;
    return 0;

print("1 represents that the rat enters the cell")
if(solveMaze(0, 0)):
    for i in sol:
        print(i)
else:
    print("No Path Exist!")
