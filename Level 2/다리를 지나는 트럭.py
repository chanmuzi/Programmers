from collections import deque

def solution(length, weight, trucks):
    # 다리 위 상황(0은 공기로 채워졌다고 가정)
    bridge = deque([0] * length)
    bridge_weight = 0 # 다리 위 무게 합
    time = 0
    
    trucks = deque(trucks) # 큐로 변경
    while trucks: # 대기 트럭이 있는 동안 반복
        wait = trucks.popleft() # 대기 1번 뽑기
        time += 1
        bridge_weight -= bridge[0] # 다리 맨 앞 원소 빼기
        bridge.popleft()
        
        # 대기 트럭이 올라갈 수 있으면
        if bridge_weight + wait <= weight:
            bridge_weight += wait
            bridge.append(wait)
        else: # 대기 트럭이 올라갈 수 없으면
            bridge.append(0)
            trucks.appendleft(wait) # 다시 대기 목록에 추가

    while bridge: # 다리 위 남은 것들을 전부 제거
        bridge.popleft()
        time += 1
    
    return time
        