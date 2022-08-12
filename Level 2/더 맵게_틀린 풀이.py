import heapq as hp

def solution(scoville, k):
    cnt = 0
    while scoville:
        if scoville[0] < k and len(scoville) >= 2:
            a = hp.heappop(scoville)
            b = hp.heappop(scoville)
            hp.heappush(scoville,a+b*2)
            cnt += 1
        elif scoville[0] >= k:
            return cnt
        elif scoville[0] < k and len(scoville) < 2:
            return -1
        else: return -1