# 경우의 수
cnt = 0
def solution(numbers, target):
    queue = []
    # dfs 정의, 리스트, 인덱스
    def dfs(queue,idx):
        # 전역 변수 가져오기
        global cnt
        # 모든 숫자 연산이 끝나면
        if len(queue) == len(numbers):
            # 그 합이 target과 같을 경우 count
            if sum(queue) == target: cnt += 1
            return
        
        # 처리할 리스트에 양수로 추가
        queue.append(numbers[idx])
        idx += 1
        dfs(queue,idx)
        # 재귀 후 기존 원소 뱉어내기
        queue.pop()
        idx -= 1
        
        # 처리할 리스트에 음수로 추가
        queue.append(-numbers[idx])
        idx += 1
        dfs(queue,idx)
        # 재귀 후 기존 원소 뱉어내기
        queue.pop()
        idx -= 1
        return
    
    # 공백 리스트, 0번 인덱스부터 시작
    dfs(queue,0)
    return cnt