def solution(board):
    def square(n,x,y):
        if board[x][y] == 0: return False
        flag = True
        for i in range(x,x+n):
            for j in range(y,y+n):
                if board[i][j] == 0:
                    flag = False
                    break
        if flag:
            return True
        else: return False
    
    len_row = len(board)
    len_col = len(board[0])

    for n in range(len_col,0,-1):
        for row in range(len_row-n+1):
            for col in range(len_col-n+1):
                if square(n,row,col): return n*n
    return 0