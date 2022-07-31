def solution(s):
    # 공백 기준으로 나누어 리스트 생성
    words = list(s.split(' '))
    for i in range(len(words)):
        # 공백이 아니고 문자로 시작하는 경우
        if words[i] != '' and words[i][0].isalpha:
            # 소문자로 변환
            words[i] = words[i].lower()
            # 첫 글자만 대문자로 변환
            words[i] = words[i].capitalize()
    # 공백으로 합치기
    return ' '.join(words)