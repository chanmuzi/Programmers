board = []
for i in range(9):
    board.append(list(map(int,input().split())))

blank = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i,j))

def row(y,z):
    for i in range(9):
        if board[i][y] == z:
            return False
    return True
    
def col(x,z):
    for i in range(9):
        if board[x][i] == z:
            return False
    return True
    
def box(x,y,z):
    nx = x//3*3
    ny = y//3*3
    for i in range(nx,nx+3):
        for j in range(ny,ny+3):
            if board[i][j] == z:
                return False
    return True

def num(count):
    if count == len(blank):
        for i in range(9):
            print(*board[i])
        exit(0)
    
    for k in range(1,10):
        x,y = blank[count]
        print(x,y)
        if row(y,k) and col(x,k) and box(x,y,k):
            board[x][y] = k
            num(count+1)
            board[x][y] = 0
            
num(0)
