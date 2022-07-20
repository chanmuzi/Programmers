def solution(x):
    # 나눌 숫자 sum 초기화
    sum = 0
    # x를 문자열로 변환한 후 그 길이만큼 반복
    for i in range(len(str(x))):
        # 각 자리의 숫자를 sum에 모두 합산
        sum += int(str(x)[i])
    # x를 sum으로 나눴을 때 나머지가 0이라면
    if x % sum == 0: answer = True
    else: answer = False
    return answer