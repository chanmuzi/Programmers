def solution(prices):
    # 정답 리스트 초기화
    answer = [0] * (len(prices))
    
    # 각 가격에 대해
    for i in range(len(prices)):
        # 카운트 초기화
        cnt = 0
        # 확인할 가격 이후와 하나씩 비교하여
        for j in range(i+1, len(prices)):
            # 이후 가격보다 작거나 같은 경우
            if prices[i] <= prices[j]: cnt += 1
            # 이후 가격보다 큰 경우
            else: 
                cnt += 1
                break
        # 정답 리스트에 기록
        answer[i] = cnt
    return answer