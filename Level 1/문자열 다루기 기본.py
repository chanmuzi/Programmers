def solution(s):
    # 문자열의 길이가 4 또는 6일 때
    if len(s) == 4 or len(s) == 6:
        # 오류 초기화
        error = 0
        # 문자열 길이만큼 반복
        for i in range(len(s)):
            # i번째 문자가 숫자면 진행
            if s[i].isdigit(): continue
            # i번째 문자가 숫자가 아니면
            else:
                # 오류 증가시키고 반복 중단
                error += 1
                break
        # 오류가 없었으면 True 반환                    
        if error == 0: return True
        # 오류가 존재하면 False 반환
        else: return False
        
    # 문자열의 길이가 4 또는 6이 아니면 False 반환        
    else: return False