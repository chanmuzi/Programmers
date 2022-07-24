# 제곱근 함수 불러오기
from math import sqrt
# 소수 리스트 생성 함수
def decimal(x):
    # x+1개만큼 True가 포함된 리스트 생성
    initial_list = [True]*(x+1)
    # 2부터 x의 제곱근까지
    for i in range(2,int(sqrt(x))+1):
        # Ture인 값들에 대해
        if initial_list[i] == True:
            # 배수를 전부 False로 변경
            for j in range(i+i,x+1,i):
                initial_list[j] = False
    
    # 모든 배수를 지우고 남은 소수들만 리스트로 반환                
    return [x for x in range(2,x+1) if initial_list[x] == True]

# 조합 함수 불러오기
from itertools import combinations
def solution(nums):
    # nums 리스트에서 3개를 뽑아 조합을 만들고, 그 합을 리스트로 생성
    cases = list(map(sum,combinations(nums,3)))
    # 경우의 수 초기화
    case = 0
    # 최댓값을 기준으로 소수 리스트 생성
    decimal_list = decimal(max(cases))
    # 조합의 합 리스트 요소에 대해
    for i in cases:
        # 그 요소가 소수 리스트에 포함되면 count
        if i in decimal_list: case += 1
    return case