from collections import deque

def solution(length, weight, trucks):
    bridge = deque([0] * length)
    time = 0
    
    trucks = deque(trucks)
    while trucks:
        wait = trucks.popleft()
        time += 1
        bridge.popleft()
        
        if sum(bridge) + wait <= weight:
            bridge.append(wait)
        else: 
            bridge.append(0)
            trucks.appendleft(wait)

    while bridge:
        bridge.popleft()
        time += 1
    
    return time
        