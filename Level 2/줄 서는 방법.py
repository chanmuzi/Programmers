def solution(n, k):
    # 숫자를 뽑을 리스트 초기화
    num_list = [x for x in range(1,n+1)]
    answer = []
    
    # 팩토리얼 DP로 구하기, n은 최대 20
    facto = [x for x in range(21)]
    facto[0] = 1
    for i in range(2,21):
        # 이전 값들과 모두 곱하기
        for j in range(2,i):
            facto[i] *= j
    
    # n이 0이 될 때까지 반복
    while n:
        # 숫자가 반복되는 기준        
        temp = facto[n] // n
        # 몫과 나머지로 구분
        index = k // temp
        k = k % temp
        # 반복의 마지막에 해당되는 경우
        if k == 0:
            answer.append(num_list.pop(index-1))
        else:
            answer.append(num_list.pop(index))
        # 다음 숫자 구하기
        n -= 1
    
    return answer