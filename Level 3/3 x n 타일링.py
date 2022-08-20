def solution(n):
    # 홀수는 취급하지 않음
    n //= 2
    # DP 테이블 초기화
    dp = [0] * (n+1)
    dp[1] = 3
    dp[2] = 11
    
    # 점화식 적용
    for i in range(3,n+1):
        dp[i] = (3 * dp[i-1] + 2*sum(dp[:i-1]) + 2) % 1000000007
    return dp[n]