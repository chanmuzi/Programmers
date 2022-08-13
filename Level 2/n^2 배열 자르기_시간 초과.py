def solution(n, left, right):
    square = [[0 for x in range(1,n+1)] for _ in range(n)]
    
    for i in range(n):
        for j in range(i+1):
            square[i][j] = i+1
    for i in range(n):
        for j in range(i+1):
            square[j][i] = i+1
    
    result = sum(square,[])
    return result[left:right+1]