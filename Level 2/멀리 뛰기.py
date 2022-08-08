def solution(n):
    # n=1 일 때 1 반환
    if n == 1: return 1
    else: 
        # DP 테이블 초기화
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        # 점화식 적용, 숫자가 커지는 것을 방지하기 위해
        # 계속해서 나머지 연산자 활용하기
        for i in range(3,n+1):
            dp[i] = (dp[i-2] + dp[i-1]) % 1234567

        # DP 테이블 마지막 값 반환
        return dp[-1]