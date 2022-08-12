def solution(number, k):
    # 스택 초기화
    stack = []
    # numbers의 모든 숫자를 검사하며 추가
    for num in number:
        # 스택의 마지막 값이 다음 값보다 작으면
        while stack and stack[-1] < num and k > 0:
            # 스택의 마지막 숫자를 제거
            k -= 1
            stack.pop()
        stack.append(num)

    # 숫자를 다 지우지 못했다면
    if k != 0:
        # 앞에서부터 자르기
        stack = stack[:-k]
        
    return ''.join(stack)