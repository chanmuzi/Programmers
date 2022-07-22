def solution(d, budget):
    # 오름차순 정렬
    d = sorted(d)
    # 개수 초기화
    count = 0
    # 리스트 요소에 대해
    for i in d:
        # 예산에서 요소만큼 뺄셈
        budget -= i
        # 예산이 음수이면 반복 종료
        if budget < 0: break
        # 그렇지 않으면 개수 증가
        count += 1
    return count