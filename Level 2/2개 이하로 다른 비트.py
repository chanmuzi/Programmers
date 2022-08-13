def solution(numbers):
    results = []
    
    for num in numbers: # 숫자마다 확인
        if num % 2 == 0: # 짝수인 경우
            results.append(num+1)
        else: # 홀수인 경우
            num = format(num,'b') # 2진수 변환
            if not '0' in num: # 0이 하나도 없는 경우
                results.append(int('10' + num[1:],2))
            else: # 0이 있는 경우
                idx = num.rfind('0')
                results.append(int(num[:idx]+'10'+num[idx+2:],2))
                
    return results