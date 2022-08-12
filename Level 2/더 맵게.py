import heapq as hp

def solution(scoville, k):
    # 오름차순 정렬
    scoville.sort()
    # 섞은 횟수 초기화
    cnt = 0
    # 리스트가 비어있지 않는 동안 반복
    while scoville:
        # 두 개 이상의 원소가 존재하고 첫 번째 원소가
        # 목표치보다 낮을 때
        if scoville[0] < k and len(scoville) >= 2:
            # 원소 두 개를 꺼내어 연산 후 다시 넣기
            a = hp.heappop(scoville)
            b = hp.heappop(scoville)
            hp.heappush(scoville,a+b*2)
            # 섞었으니 카운트
            cnt += 1
        # 첫 번째 원소가 목표치 이상이면 누적 카운트 return
        elif scoville[0] >= k:
            return cnt
        # 연산할 원소가 없는데 목표치 미만이면 불가능
        elif scoville[0] < k and len(scoville) < 2:
            return -1
        # 그 이외도 불가능한 케이스
        else: return -1