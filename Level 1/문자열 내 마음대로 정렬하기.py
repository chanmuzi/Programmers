def solution(strings, n):
    # 문자열 오름차순 정렬
    strings.sort()
    # 인덱스 n을 기준으로 정렬
    strings.sort(key=lambda x:x[n])
    return strings