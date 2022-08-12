def solution(s):
    stack = []
    
    for i in range(len(s)):
        # 여는 괄호는 스택에 쌓기
        if s[i] == '(':
            stack.append('(')
        elif s[i] == '[':
            stack.append('[')
        # 닫힌 괄호일 경우
        elif s[i] == ')':
            # 스택이 비어있거나 직전이 다른 모양의 여는 괄호인 경우
            if not stack or s[i-1] == '[':
                stack.append('x')
                break
            # 짝이 맞으면 스택 비우기
            stack.pop()
        else:
            if not stack or s[i-1] == '(':
                stack.append('x')
                break
            stack.pop()
    
    # 스택이 비어있지 않으면 False
    if stack: return False
    else: return True