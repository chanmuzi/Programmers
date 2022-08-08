def solution(begin, end):
    arr = [0 for _ in range(end+1)]
    arr[0] = 0
    
    for i in range(1,end+1):
        for j in range(2*i,end+1,i):
            arr[j] = i
            
    return arr[begin:end+1]