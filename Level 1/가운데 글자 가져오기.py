def solution(s):
    # 문자열의 길이가 홀수이면
    if len(s) % 2 != 0: answer = s[len(s)//2]
    # 문자열의 길이가 짝수이면
    else: answer = s[(len(s)//2)-1] + s[len(s)//2]
    return answer