def solution(s):
    # 한 개 이상의 공백을 기준으로 분할
    word_list = s.split(' ')
    # 정답 리스트 초기화
    answer_list = []
    
    # 단어의 개수만큼 반복
    for i in range(len(word_list)):
        # 공백 리스트 추가
        answer_list.append([])
        # 각 단어의 길이만큼 반복
        for j in range(len(word_list[i])):
            # 짝수 번째 일때는 대문자를 정답 리스트에 추가
            if j % 2 == 0: answer_list[i].append(word_list[i][j].upper())
            # 홀수 번째 일때는 소문자를 정답 리스트에 추가
            else: answer_list[i].append(word_list[i][j].lower())
    
    # 문자열 리스트 초기화        
    str_list = []
    # 정답 리스트에 포함된 각 리스트마다
    for i in answer_list:
        # 그 리스트의 요소를 문자열로 합쳐 문자열 리스트에 추가
        str_list.append(''.join(i))
    
    # 문자열 리스트의 모든 요소들을 공백으로 합쳐 문자열 생성
    answer = ' '.join(str_list)
    return answer