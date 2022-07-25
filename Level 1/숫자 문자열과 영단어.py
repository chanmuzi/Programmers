def solution(s):
    # 숫자 딕셔너리 생성
    num_dict = {'zero':0,'one':1,'two':2,
               'three':3,'four':4,'five':5,
               'six':6,'seven':7,'eight':8,
               'nine':9}
    answer = ''
    temp = ''
    
    # 문자열의 각 요소에 대해
    for i in list(s):
        # 숫자면 정답에 그대로 추가
        if i.isdigit(): answer += i
        # 문자면
        else: 
            # 임시 문자열에 추가
            temp += i
            # 임시 문자열이 딕셔너리에 존재하면
            if temp in num_dict: 
                # 정답 리스트에 value 추가
                answer += str(num_dict[temp])
                # 임시 문자열 초기화
                temp = ''
    
    # 정수형으로 변경하여 반환
    return int(answer)