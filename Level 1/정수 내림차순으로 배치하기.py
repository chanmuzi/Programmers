def solution(n):
    # 입력 문자를 리스트로 변환
    n_list = list(str(n))
    # 내림차순 정렬
    n_list.sort(reverse=True)
    # 리스트를 문자열로 변환
    reversed_n = ''.join(n_list)
    # 정수형으로 변환하여 반환
    return int(reversed_n)
