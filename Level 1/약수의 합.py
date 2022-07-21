# 제곱근 함수 불러오기
from math import sqrt

def solution(n):
    # 약수 리스트 초기화
    mean_list = []
    # n의 제곱근까지 반복
    for i in range(1,int(sqrt(n))+1):
        # 나머지가 0인 경우
        if n % i == 0:
            # 그 값을 추가
            mean_list.append(i)
            # 나눗값과 몫이 동일하지 않을 경우 몫도 추가
            if i**2 != n: mean_list.append(n//i)
    
    # 리스트의 총합
    answer = sum(mean_list)
    return answer