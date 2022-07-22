def solution(n):
    # 문자열 초기화
    tmp = ''
    # n이 0이 될 때까지
    while n:
        # 나머지를 문자열에 추가
        tmp += str(n % 3)
        # n은 몫으로 갱신
        n = n // 3
    # 문자열을 3진법 정수형으로 변환
    answer = int(tmp, 3)
    return answer