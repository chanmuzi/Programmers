import bisect as bi

def solution(citations):
    # 오름차순 정렬
    citations.sort()
    n = len(citations)
    h_index = 0

    # 논문 수만큼 반복
    for i in range(n):
        # i 이하, 이상을 구할 인덱스
        temp_max = bi.bisect_right(citations,i)
        temp_min = bi.bisect_left(citations,i)

        # 문제의 조건 만족시 h-index 갱신
        if i <= (n-temp_min) and i >= temp_max:
            h_index = i
    return h_index