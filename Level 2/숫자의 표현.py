def solution(n):    
    cnt = 1
    for i in range(1,n//2+2):
        for j in range(i+1,n//2+2):
            if (i+j)/2 *(j-i+1) > n: break
            elif (i+j)/2 *(j-i+1) == n:
                cnt += 1
    return cnt
