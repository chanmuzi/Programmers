def solution(prices):
    # 리스트의 길이
    length = len(prices)
    
    # answer을 max값으로 초기화  
    answer = [ i for i in range (length - 1, -1, -1)]
    
    # 주식 가격이 떨어질 경우 찾기
    stack = [0]
    for i in range (1, length):
        # 스택이 비어있지 않고
        # 스택의 마지막 인덱스의 가격이 이번에 확인하는 인덱스의 가격보다 크다면
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        # 이번 인덱스도 스택에 추가
        stack.append(i)
    return answer