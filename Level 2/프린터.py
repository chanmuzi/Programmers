from collections import deque

def solution(priorities, location):
    # (인덱스,중요도)로 리스트 재구성
    priorities = deque([(x,priorities[x]) for x in range(len(priorities))])
    cnt = 0
    
    # 계속 반복
    while True:
        # 인덱스,중요도 뽑아내기
        idx,priority = priorities.popleft()
        # 나머지 원소들과 비교하여
        for i in priorities:
            # 중요도 더 큰 것이 있으면
            if i[1] > priority:
                # 맨 뒤로 보내고 다시 반복
                priorities.append((idx,priority))
                break
        # 중요도 더 큰 것이 발견되지 않으면
        else: 
            cnt += 1 # 카운트
            # 확인하려던 원소면 쌓인 카운트 반환
            if idx == location: return cnt
