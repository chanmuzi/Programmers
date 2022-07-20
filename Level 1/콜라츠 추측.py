def solution(num):
    # 횟수 초기화
    count = 0
    # 500회가 되거나 숫자 1이 될 때까지
    while (count != 500) and (num != 1):
        # 매회 카운트 1씩 증가
        count += 1
        # 짝수면 2로 나누고
        if num % 2 == 0: num //= 2
        # 홀수면 3을 곱한뒤 1을 더하기
        else: num = num*3 + 1
    # 최종 결과가 1이면 횟수 반환
    if num == 1: return count
    # 500회를 모두 수행해도 1이 아니면
    else: return -1