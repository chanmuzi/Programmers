from math import sqrt
def solution(left, right):
    # 제곱근의 정수형을 제곱한 것이 기존의 숫자와 같으면 음수로, 그렇지 않으면 양수로 구해 합산
    return sum([-x if int(sqrt(x))**2 == x else x for x in range(left,right+1)])