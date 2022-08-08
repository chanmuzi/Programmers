def solution(begin, end):
    arr = [True for x in range(end+1)]
    for i in range(2, int(end**0.5)+1):
        if arr[i]:
            for j in range(i+i,end+1,i):
                arr[j] = False
    
    sosu = [x for x in range(2,end+1) if arr[x] == True]
    
    answer = []
    for i in range(begin,end+1):
        if i in sosu:
            answer.append(1)
        elif i == 1: answer.append(0)
        else:
            for j in range(i-1,1,-1):
                if i % j == 0:
                    answer.append(j)
                    break
    return answer