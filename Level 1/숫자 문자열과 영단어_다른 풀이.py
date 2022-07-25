def solution(s):
    # 숫자 리스트 생성
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    # 숫자 리스트의 각 요소에 대해
    for i in range(len(words)):
        # 문자열 내에 존재하는 문자열을 정수형 숫자로 변경
        s = s.replace(words[i], str(i))

    return int(s)