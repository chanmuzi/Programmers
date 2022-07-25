def solution(new_id):
    # 1. 소문자로 변환하기
    new_id = new_id.lower()
    result = []
    special = ['-','_','.']
    
    # 2. 알파벳, 숫자, 빼기, 밑줄, 마침표만 result에 추가
    for i in new_id:
        if i.isdigit() or i.isalpha() or i in special:
            result.append(i)
            
    answer = []
    # 3. 연속된 마침표 제거하기
    for i in range(len(result)-1):
        if result[i] == '.' and result[i+1] == '.': continue
        else: answer.append(result[i])
    # 리스트 길이가 1이면
    if len(result) == 1:
        # 그대로 추가(위 반복문이 수행되지 않았으므로)
        answer.append(result[0])
    # 마지막 요소는 반드시 추가
    else: answer.append(result[-1])

    # 4. 처음, 마지막 마침표 제거
    if len(answer) != 0 and answer[0] == '.':
        answer.remove('.')
    if len(answer) != 0 and answer[-1] == '.':
        answer.pop()

    # 5. 빈 문자열에 'a' 추가
    if len(answer) == 0: answer.append('a')
    
    # 6. 16자 이상 문자열 자르기
    if len(answer) >= 16: answer = answer[0:15]
    # 마지막이 '.'이면 제거하기
    if len(answer) != 0 and answer[-1] == '.':
        answer.pop()
    
    # 7. 길이가 3이 될 때까지 마지막 요소 추가
    if len(answer) <= 2:
        while len(answer) != 3:
            answer.append(answer[-1])
    
    # 문자열로 반환
    return ''.join(answer)