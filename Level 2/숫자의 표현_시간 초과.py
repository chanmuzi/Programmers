def solution(n):
    cnt = 1
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if (i+j)/2 *(j-i+1) == n:
                cnt += 1
    return cnt
