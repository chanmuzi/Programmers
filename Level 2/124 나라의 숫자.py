def solution(n):
    answer = []
    # n이 0이 될 때까지
    while n:
        # 3으로 나눈 나머지를 저장
        temp = n % 3
        # 3으로 딱 나눠 떨어지는 숫자
        if temp == 0:
            # 0 대신 4로 저장
            temp = 4
            # n값 조정
            n -= 1
        # 문자열로 추가 후 n은 몫으로 갱신
        answer.append(str(temp))
        n //= 3
    # 뒤집고 join
    answer.reverse()
    return ''.join(answer)