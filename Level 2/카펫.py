# 제곱근 함수 불러오기
from math import sqrt

def solution(brown, yellow):
    # 약수 리스트 초기화
    measure_list = []
    # yellow의 제곱근까지
    for i in range(1,int(sqrt(yellow))+1):
        # 나머지가 0인 정수가 있다면
        if yellow % i == 0:
            # 그 정수와 yellow를 정수로 나눈 몫을 약수로 추가
            measure_list.append(i)
            measure_list.append(yellow//i)
    # 약수 리스트 오름차순 정렬
    measure_list.sort()
    # 약수 리스트의 각 요소에 대해
    for i in measure_list:
        # row는 세로줄의 수, column은 가로줄의 수
        row = i
        column = yellow // i
        # 세로가 가로보다 길면 다른 case로 넘어가기
        if row > column: continue
        # 가로 >= 세로의 경우
        else:
            # yellow를 둘러싸는 사각형 - yellow 사각형 = yellow를 둘러싸는 테두리
            if ((row+2)*(column+2))-yellow == brown: return [column+2, row+2]
            else: continue