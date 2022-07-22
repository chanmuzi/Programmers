from collections import Counter
def solution(s):
    # 문자열 내의 문자 개수를 파악해 딕셔너리 생성
    alpha_count = Counter(s)
    # p와 y의 개수가 같을 때만 True 반환
    if alpha_count['p'] + alpha_count['P'] == alpha_count['y'] + alpha_count['Y']:
        return True
    else: return False