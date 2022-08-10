from itertools import permutations

# 소수 판별 함수
def prime(n):
    # 0,1 은 소수 x
    if n == 1 or n == 0: return False

    # n의 제곱근까지 약수 존재하면 소수 x
    for i in range(2,int(n**0.5)+1):
        if n % i == 0: return False
    
    # 반복문 통과 후 소수 o
    return True

def solution(numbers):
    # 카운트, 숫자 조합 초기화
    cnt = 0
    case = []

    num_list = list(map(int,numbers))
    # 숫자 개수만큼 반복
    for i in range(1,len(num_list)+1):
        # 순열을 구하고 중복 제거
        temp = list(set(permutations(num_list,i)))
        # 각 숫자 조합에 대해
        for j in temp:
            string = ''
            # 임시 문자열 생성 후 case에 추가
            for k in range(len(j)):
                string += str(j[k])
                case.append(string)
    
    # 중복 제거
    case = list(set(case))
    # 숫자로 바꾸고 중복 제거
    case = list(set([int(x) for x in case]))
    
    # 각 숫자에 대해 소수 판별
    for i in case:
        # 소수라면 카운트
        if prime(i): 
            cnt += 1
            print(i)
            
    return cnt