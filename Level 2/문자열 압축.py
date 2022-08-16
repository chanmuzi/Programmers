def solution(s):
    answer = len(s) # 문자열 길이가 default
    
    for step in range(1,len(s)):
        prev = s[:step] # 비교할 문자열
        cur = "" # 현재 step에서 만들어진 압축 문자열
        cnt = 1  # 같은 문자열의 개수
        
        # 비교 문자열의 길이만큼
        for i in range(step,len(s),step):
            # 비교 문자열과 같으면
            if prev == s[i:i+step]:
                cnt += 1
            # 비교 문자열과 같지 않으면
            else:
                if cnt >= 2: # 연속되었던 경우
                    cur += str(cnt) + prev
                else: # 연속되지 않았던 경우
                    cur += prev
                prev = s[i:i+step] # 비교 문자열 초기화
                cnt = 1 # 같은 문자열 개수 초기화
        
        # 마지막 남은 문자열 추가
        if cnt >= 2:
            cur += str(cnt) + prev
        else:
            cur += prev
        # 문자열 최소 길이 갱신
        answer = min(answer,len(cur))
    
    return answer