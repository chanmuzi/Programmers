# 제곱근 함수 불러오기
from math import sqrt

def solution(n):
    # 제곱근 구하기
    test_n = sqrt(n)
    # 제곱근을 정수로 변환하고 제곱한 값이 기존의 n과 같으면
    # (제곱근+1)의 제곱 반환
    if int(test_n)**2 == n: return (int(test_n)+1)**2
    # 그렇지 않으면 -1 반환
    else: return -1