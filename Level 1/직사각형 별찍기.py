def solution(operations):
    # 정답 리스트 초기화
    answer = []
    # 입력 받은 연산 횟수만큼 반복
    for i in range(len(operations)):
        # 최솟값 제거 연산
        if operations[i] == "D -1":
            if len(answer) == 0: continue
            else: answer.remove(min(answer))
        # 최댓값 제거 연산
        elif operations[i] == "D 1":
            if len(answer) == 0: continue
            else: answer.remove(max(answer)) 
        # 리스트에 요소 추가    
        else:
            # 문자와 숫자를 나누어 숫자만 추가
            a,b = operations[i].split()
            answer.append(int(b))
    # 리스트가 비어 있으면 [0,0] 출력
    if len(answer) == 0: return [0,0]
    # 그렇지 않으면
    else:
        # 최댓값, 최솟값 출력
        return [max(answer),min(answer)]