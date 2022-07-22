# 제곱근 함수 불러오기
from math import sqrt 

def solution(n):
    # 테라토스테네스의 체 알고리즘
    index_list = [True for i in range(n+1)]
    # 루트 n 범위까지 반복(1은 제외)
    for i in range(2,int(sqrt(n))+1):
        # i번째 정수가 True라면
        if index_list[i] == True:
            # 그 정수의 배수를 False 처리
            for j in range(i+i,n+1,i):
                index_list[j] = False
    
    # 최종 리스트 초기화                
    result_list = []
    # 2부터 n까지
    for i in range(2,n+1):
        # True로 남아있는 값들만 최종 리스트에 추가
        if index_list[i] == True:
            result_list.append(i)
    
    # 최종 리스트의 길이 반환            
    answer = len(result_list)
    return answer