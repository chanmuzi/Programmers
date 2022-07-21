def solution(n):
    # n을 문자열로 변환후 리스트로 변환
    answer = list(str(n))
    # 역순으로 재배치
    answer = reversed(answer)
    # 리스트의 모든 요소들을 정수형으로 변환
    answer = [int(x) for x in answer]
    return answer