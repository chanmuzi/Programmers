def solution(n):
    # n이 짝수이면
    if n % 2 == 0:
        # n/2 만큼 '수박' 반환
        answer = '수박'*(n//2)
    # n이 홀수이면        
    else:
        # n/2 반올림하고 끝에 '수' 붙여주기
        answer = '수박'*(n//2) + '수'
    return answer