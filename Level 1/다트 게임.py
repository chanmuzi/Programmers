def solution(dartResult):
    # 스택 초기화
    stack = []
    # 10을 A로 치환
    dartResult = dartResult.replace("10", "A")
    # 보너스 딕셔너리 생성
    bonus = {'S': 1, 'D': 2, 'T': 3}
    
    # 각 문자에 대해
    for i in dartResult:
        # 숫자면 스택에 추가
        if i.isdigit() or i=='A':
            stack.append(10 if i == 'A' else int(i))
        # 연산 문자면 딕셔너리의 key로 이용하여 제곱
        elif i in ('S', 'D', 'T'):
            # 스택의 마지막 요소 꺼내기
            num = stack.pop()
            # 연산 후 스택에 다시 추가
            stack.append(num ** bonus[i])
        # '#'인 경우            
        elif i == '#':
            # 스택의 마지막 요소 음수로 변환
            stack[-1] *= -1
        # '*'인 경우
        elif i == '*':
            # 스택의 마지막 요소 꺼내기
            num = stack.pop()
            # 스택이 비어있지 않다면
            if len(stack):
                # 스택의 마지막 요소 두배 연산
                stack[-1] *= 2
            # 두배 연산 후 스택에 다시 추가
            stack.append(2 * num)
    # 스택에 저장된 숫자 세 개 합산            
    return sum(stack)