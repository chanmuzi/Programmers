def solution(sizes):
    # sizes의 각 요소중 큰 것과 작은 것들을 나누고, 그 중 각각 가장 큰 것들을 곱함
    return max([max(x) for x in sizes]) * max([min(x) for x in sizes])