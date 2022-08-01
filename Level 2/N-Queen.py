# queen 함수 반복문의 x행 i열에 queen 배치가 가능한지 확인
def check(x,row):
    # x 이전의 행까지만 비교
    for i in range(x):
        # 같은 열에 위치 or 대각선 위치
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return False
    # 어떤 경우에도 해당되지 않으면 True
    return True

# 경우의 수 저장 변수
answer = 0 
def queen(x,n,row):
    global answer
    # 모든 행에 대해 queen 배치가 끝나면
    if x == n:
        # 경우의 수 +1 후 함수 종료
        answer += 1
        return
    
    for i in range(n):
        row[x] = i
        # 놓을 수 있는 위치로 확인되면
        if check(x,row):
            # 다음 행에 대해 queen 재귀함수
            queen(x+1,n,row)
            
def solution(n):
    # 행마다 열 위치를 기록할 리스트 초기화
    row = [0]*n
    # 0번 인덱스 행부터 시작
    queen(0,n,row)
    return answer