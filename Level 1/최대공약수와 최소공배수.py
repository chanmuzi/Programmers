# 최대공약수 함수 불러오기
from math import gcd
def solution(n,m):
    # 정답 리스트 초기화
    answer = []
    # 최대공약수 구하기
    gcd_ = gcd(n,m)
    # 최소공배수 구하기
    lcm = n * m // gcd_
    # 정답 리스트에 추가
    answer.extend([gcd_,lcm])
    return answer