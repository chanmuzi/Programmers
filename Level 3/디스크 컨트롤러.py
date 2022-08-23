import heapq as hq

def solution(jobs):
    start = -1 # 직전에 완료한 작업의 시간
    answer,now,idx = 0,0,0 # 정답,현재 시간,인덱스
    heap = []
    
    jobs.sort() # 오름차순 정렬
    
    while idx < len(jobs): # jobs의 모든 원소를 순회
        
        for job in jobs[idx:]: # 현재 인덱스 이후의 것들만 확인
            # 작업 요청 시간이 범위를 충족할 경우
            if start < job[0] <= now: 
                hq.heappush(heap,[job[1],job[0]])
        
        if heap: # 힙에 아직 처리하지 않은 원소가 있다면
            cur = hq.heappop(heap)
            start = now # 직전에 완료한 작업의 시간
            now += cur[0] # 현재 시간 증가
            answer += now - cur[1] # 완료 - 요청
            idx += 1 # 인덱스 증가
        # 힙에 처리할 원소가 없었다면 시간을 증가
        else: now += 1
    
    return int(answer / len(jobs))