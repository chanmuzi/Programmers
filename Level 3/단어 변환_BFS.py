from collections import deque

# 다른 글자 개수를 세는 함수
def check(x,y):
    cnt = 0
    
    for i in range(len(x)):
        if x[i] != y[i]: cnt += 1
    return cnt

def solution(begin, target, words):
    
    # 변환할 수 없는 경우
    if target not in words: return 0
    
    # 방문 리스트 초기화
    visited = [False] * (len(words))
    
    q = deque([])
    q.append((begin,0)) # 시작 글자, 변환 횟수
    while q:
        word,cnt = q.popleft()
        
        # 단어가 target이 되면 누적된 cnt 반환
        if word == target: return cnt
        
        for i in range(len(words)):
            # 다른 글자 개수가 1개이면
            if check(word,words[i]) == 1:
                # 방문 처리후 그 문자를 기준으로 탐색 시작
                visited[i] = True
                q.append((words[i],cnt+1))
                