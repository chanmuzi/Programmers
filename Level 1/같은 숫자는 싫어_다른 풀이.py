def solution(s):
    # 정답 리스트 초기화
    a = []
    # 입력 받은 리스트의 각 요소에 대해
    for i in s:
        # i부터 끝까지 같은 것이 지속될 동안은 패스
        if a[-1:] == [i]: continue
        # 같은 것이 없을 때는 추가
        a.append(i)
    return a