def solution(absolutes, signs):
    # 정답 초기화
    answer = 0
    # absolutes 리스트 길이만큼 반복
    for i in range(len(absolutes)):
        # sign이 참이면
        if signs[i] == True:
            # 정답에 덧셈
            answer += absolutes[i]
        # 그렇지 않으면    
        else:
            # 정답에 뺄셈
            answer -= absolutes[i]
    return answer