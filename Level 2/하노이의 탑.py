def hanoi(x,start,aux,end):
    global answer
    # 종료 조건
    if x == 1:
        answer.append([start,end])
        return
    
    # x-1개를 보조에 먼저 옮기기
    hanoi(x-1,start,end,aux)
    # 남은 1개를 목표에 옮기기
    answer.append([start,end])  
    # 보조의 x-1개를 목표로 옮기기
    hanoi(x-1,aux,start,end)
    
answer = []
def solution(n):
    # n,시작,보조,목표
    hanoi(n,1,2,3)
    return answer
