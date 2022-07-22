def solution(s):
    # 숫자 리스트 초기화
    ord_list = []
    # 문자열 길이만큼 반복
    for i in range(len(s)):
        # 문자를 숫자로 바꾸어 리스트에 추가
        ord_list.append(ord(s[i]))
    # 숫자 리스트 내림차순 정렬
    ord_list.sort(reverse=True)
    
    # 문자열 리스트 초기화
    chr_list = []
    # 숫자 리스트의 요소들을
    for i in ord_list:
        # 문자로 바꾸어 문자열 리스트에 추가
        chr_list.append(chr(i))
    # 리스트 요소들을 공백 없이 합쳐 문자열로 반환    
    answer = ''.join(chr_list)
    return answer