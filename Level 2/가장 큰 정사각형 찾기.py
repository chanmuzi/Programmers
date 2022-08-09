def solution(board):
    # DP 테이블을 열,행 기준으로 초기화
    dp = [[0]* (len(board[0])+1) for _ in range(len(board)+1)]
    # 정사각형 사이즈 초기화
    n = 0
    # DP 테이블은 정수 그대로, 기존 board는 인덱스로 접근
    for i in range(1, len(board)+1):
        for j in range(1, len(board[0])+1):
            # board의 값이 1일 때
            if board[i-1][j-1] == 1:
                # DP 테이블의 값 = 위쪽, 왼쪽, 왼쪽 위 중 최솟값 + 1
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                # 기존 최댓값보다 크면 갱신
                if dp[i][j] > n :
                    n = dp[i][j]

    # 정사각형 크기 반환
    return n**2