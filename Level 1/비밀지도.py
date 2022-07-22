def solution(n, arr1, arr2):
    # 2진수 리스트 초기화
    arr1_bi = []
    arr2_bi = []
    # n번 반복
    for i in range(n):
        # 배열의 각 요소를 2진수로 변환
        temp = format(arr1[i],'b')
        # 오른쪽 정렬, 빈공간은 0으로 채우기
        temp = temp.rjust(n,'0')
        # 결과값을 리스트로 변환하여 2진수 리스트에 추가
        arr1_bi.append(list(map(int,temp)))
        # 배열의 각 요소를 2진수로 변환
        temp = format(arr2[i],'b')
        # 오른쪽 정렬, 빈공간은 0으로 채우기
        temp = temp.rjust(n,'0')
        # 결과값을 리스트로 변환하여 2진수 리스트에 추가
        arr2_bi.append(list(map(int,temp)))

    # 최종 리스트 초기화, n만큼 공백리스트 생성
    result_list = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 이중 리스트의 두 요소가 0일 때만
            if (arr1_bi[i][j] == 0) and (arr2_bi[i][j] == 0):
                # 공백을 추가
                result_list[i].append(' ')
            # 하나라도 0이 아니면 '#'을 추가
            else: result_list[i].append('#')
    
    # 결과 리스트의 각 요소를 공백 없이 합쳐 반환
    answer = [''.join(x) for x in result_list]
    return answer