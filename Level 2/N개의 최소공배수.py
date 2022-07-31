# 최대공약수 함수 불러오기
from math import gcd

def solution(arr):
    # 첫 최소공배수
    lcm = arr[0]
    # 리스트의 끝에서 두 번째까지
    for i in range(len(arr)-1):
        # 최소공배수 = 현재 최소공배수 * 다음 원소 // 둘의 최대공약수
        lcm = lcm * arr[i+1] // gcd(lcm, arr[i+1])
    return lcm