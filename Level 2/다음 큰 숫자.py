def solution(n):
    # n을 2진수로 표현 후 1의 개수 세기
    a = format(n,'b')
    a1 = str(a).count('1')
    # 문제에서 주어진 숫자 범위까지
    for i in range(n+1,1000000):
        # 2진수로 표현 후 1의 개수 세기
        b = format(i,'b')
        b1 = str(b).count('1')
        # 10진수로 바꿔서 반환
        if a1 == b1: return int(b,2)
        