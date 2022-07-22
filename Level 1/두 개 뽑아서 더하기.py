# 조합 불러오기
from itertools import combinations

def solution(numbers):
    # numbers에서 2개 뽑아 조합 만들기
    my_list = combinations(numbers,2)
    # 리스트에 저장된 각 튜플의 합을 리스트로 만든 후
    # 세트로 중복을 제거한 뒤 다시 리스트로 만들며 오름차순 정렬
    return sorted(list(set([sum(x) for x in my_list])))