def solution(s):
    # 정답 리스트 초기화
    a = []
    # 입력 받은 리스트의 각 요소에 대해
    for i in s:
        # 정답 리스트의 맨 마지막 요소와 같다면 패스
        if a[-1:] == [i]: continue
        # 같지 않을 때는 추가
        a.append(i)
    return a