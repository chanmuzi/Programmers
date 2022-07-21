def solution(s, n):
    # 문자열을 리스트로 저장
    char_list = list(s)
    # 리스트의 길이만큼 반복
    for i in range(len(char_list)):
        # 리스트의 i번째 요소가 문자라면
        if char_list[i].isalpha():
            # i번째 요소가 원래 대문자 알파벳이고 유니코드 숫자에 n을 더한 값이
            # 대문자 범위를 넘어가는 경우, 알파벳 순환 숫자인 26을 뺄셈
            if (ord(char_list[i])+n)> 90 and 65<=ord(char_list[i])<=90:
                char_list[i] = chr(ord(char_list[i])+n-26)
            # i번째 요소가 원래 소문자 알파벳이고 유니코드 숫자에 n을 더한 값이
            # 소문자 범위를 넘어가는 경우, 알파벳 순환 숫자인 26을 뺄셈                
            elif ord(char_list[i])+n > 122 and 97<=ord(char_list[i])<=122:
                char_list[i] = chr(ord(char_list[i])+n-26)
            # n을 더해도 주어진 대소문자 범위를 초과하지 않는 알파벳일 경우    
            else:
                char_list[i] = chr(ord(char_list[i])+n)            
    # 리스트의 요소들을 공백없이 합쳐 문자열로 반환                 
    answer = ''.join(char_list)
    return answer