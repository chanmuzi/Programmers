def solution(arr1, arr2):
    answer = []
    # 앞 행렬의 행
    for row in range(len(arr1)):
        temp = []
        # 뒷 행렬의 열
        for col2 in range(len(arr2[0])):
            num = 0
            # 뒷 행렬의 행
            for col1 in range(len(arr2)):
                # 앞 행렬 행 x 뒷 행렬 열
                num += arr1[row][col1] * arr2[col1][col2]
            temp.append(num)
        answer.append(temp)    

    return answer