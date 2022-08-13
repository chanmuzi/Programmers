def solution(arr):
    # 사각형 한 변의 길이
    l = len(arr)
    result = [0,0] # 0,1의 개수
    
    def dfs(x,y,l):
        # 0 또는 1
        num = arr[x][y]
        
        # 사각형 검사
        for i in range(x,x+l):
            for j in range(y,y+l):
                # 시작값과 다른게 있으면 4분할
                if arr[i][j] != num:
                    l //= 2
                    
                    dfs(x,y,l)
                    dfs(x+l,y,l)
                    dfs(x,y+l,l)
                    dfs(x+l,y+l,l)
                    return
                
        # 0 또는 1 카운트
        result[num] += 1
    
    dfs(0,0,l) # 0,0에서 시작
    return result