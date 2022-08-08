def solution(land):
    dp = land[0]
    for i in range(1,len(land)):
        for j in range(4):
            temp = 0
            for k in range(4):
                if j != k and temp < land[i][k]:
                    temp = land[i][k]
            dp[j] += temp
    return max(dp)   