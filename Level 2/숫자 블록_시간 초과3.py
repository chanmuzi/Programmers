def solution(begin, end):
    def good(x):  
        if x == 1: return 0
        for i in range(2,int(x**0.5)+1):
            if x % i == 0:
                if x // i > maximum: break
                else: return x // i
        return 1
    
    maximum = 10**7
    arr = []
    for i in range(begin,end+1):
        arr.append(good(i))
    return arr