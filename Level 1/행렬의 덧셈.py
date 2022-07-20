def solution(arr1, arr2):
    # 정답 리스트 초기화
    answer = []
    # 행의 개수만큼 반복
    for i in range(len(arr1)):
        # 정답 리스트에 행 추가
        answer.append([])
        # 열의 개수만큼 반복
        for j in range(len(arr1[i])):
            # 행렬 각 요소 더하기
            answer[i].append(arr1[i][j]+arr2[i][j])
    return answer