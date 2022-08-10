cnt = 0
answer = ''

def dfs(queue,word):
    global cnt,answer
    # 리스트가 동일하면 정답 갱신 후 종료
    if queue == word:
        answer = cnt
        return
    
    # 길이가 5가 되면 종료
    if len(queue) == 5:
        return
    
    # a,e,i,o,u 순서로 추가
    alpha = ['A','E','I','O','U']
    for i in range(5):
        # 추가할 때마다 카운트
        cnt += 1
        queue.append(alpha[i])
        dfs(queue,word)
        # 재귀 후 원상태로 복귀
        queue.pop()
    return

def solution(word):
    # 비교를 위해 단어를 리스트로 변경
    word = list(word)
    queue = []
    # 공백 리스트와 타겟 삽입
    dfs(queue,word)
    return answer