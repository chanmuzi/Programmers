results = [] # 변환 횟수를 담을 리스트

# 다른 글자 개수를 담을 리스트
def check(a,b):
    cnt = 0
    
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    return cnt


def solution(begin, target, words):
    
    # 변환이 불가능한 경우
    if target not in words:
        return 0
    
    # 방문 리스트 초기화
    visited = [False] * (len(words))

    def dfs(word,cnt):
        # 단어가 target이 되면 누적된 count 추가
        if word == target:
            results.append(cnt)
            return
        
        for i in range(len(words)):
            # 방문한적 있으면 패스
            if visited[i]: continue
            
            # 다른 글자가 한 개면
            if check(word,words[i]) == 1:
                visited[i] = True
                dfs(words[i],cnt+1)
                # 원 상태로 되돌리기(백트랙킹)
                visited[i] = False
    
    dfs(begin,0)

    # 가장 작은 것 반환
    answer = min(results)
    return answer
