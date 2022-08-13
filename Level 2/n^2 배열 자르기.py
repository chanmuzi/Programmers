def solution(n, left, right):
    answer = []
    # left부터 right까지
    for i in range(left,right+1):
        # i를 n으로 나눈 몫과 나머지 중 더 큰 값+1을 추가
        answer.append(max(i//n,i%n)+1)
    return answer