from itertools import permutations

def solution(k, dungeons):
    # 방문할 순서 조합 만들기
    numbers = list(x for x in range(0,len(dungeons)))
    cases = permutations(numbers,len(dungeons))
    
    # 최종 결과 리스트 
    results = []
    # 각 조합에 대해
    for case in cases:
        # 방문한 던전 수, 현재 피로도
        cnt = 0
        cur = k
        # 인덱스를 불러와서
        for idx in case:
            # 최소 피로도, 소모 피로도 저장
            mini,req = dungeons[idx][0],dungeons[idx][1]
            # 최소 피로도 이상 보유 중이라면 처리
            if cur >= mini:
                cur -= req
                cnt += 1
            else: break
        # 던전 수를 결과 리스트에 추가
        results.append(cnt)
    # 결과 리스트 중 가장 큰 값 반환
    return max(results)