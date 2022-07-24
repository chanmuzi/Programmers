def solution(array, commands):
    # 정답 리스트 초기화
    answer = []
    for i in commands:
        # i부터 j번째 요소 중 k번째를 temp에 저장
        temp = sorted(array[i[0]-1 : i[1]])[i[2]-1]
        # 정답 리스트에 추가
        answer.append(temp)
    return answer