def solution(arr, divisor):
    # 입력 받은 배열의 원소 중 divisor로 나눈 나머지가 0인 것들만 추가
    answer = [x for x in arr if x % divisor == 0]
    # 공백 리스트이면 [-1] 반환
    if len(answer) == 0: return [-1]
    # 요소가 있으면 정렬하여 반환
    else: return sorted(answer)