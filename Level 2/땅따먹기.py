def solution(land):
    # land의 첫 번째 행을 DP 테이블로 초기화
    dp = land[0]
    # 두 번째 행부터 마지막 행까지
    for i in range(1,len(land)):
        temp = []
        # 검사할 행의 각 열
        for j in range(4):
            maximum = 0
            # DP 테이블에 저장된 값 중 최댓값 구하기
            for k in range(4):
                if j != k and dp[k] > maximum:
                    maximum = dp[k]
            # 검사할 행의 열과 다른 DP 테이블의 열 중 최댓값 저장
            temp.append(maximum)
        # 저장된 최댓값을 검사한 행의 각 열에 맞추어 덧셈
        dp = [temp[x] + land[i][x] for x in range(4)]
    # 마지막 행까지 수행 후 최댓값 반환
    return max(dp)          