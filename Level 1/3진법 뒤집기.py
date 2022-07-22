def solution(n):
    # 3진수 리스트 초기화
    three_num = []
    # n이 0이 될 때까지
    while n:
        # 나머지를 리스트에 추가
        temp = n % 3
        # 몫으로 갱신
        n //= 3
        three_num.append(temp)
    # 리스트 첫 요소부터 3의 제곱을 적절히 곱해주며 리스트를 구하고 그 요소들을 전부 합산
    return sum([3**x*three_num[len(three_num)-1-x] for x in range(len(three_num))])