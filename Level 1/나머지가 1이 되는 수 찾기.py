def solution(n):
    # 2부터 n-1까지
    for i in range(2,n):
        # 나머지가 1인 i를 반환
        if n % i == 1: return i