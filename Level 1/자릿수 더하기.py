def solution(n):
    # 자연수를 문자열로 바꾼 뒤 정수형으로 변환하며 리스트로 생성
    # 리스트의 각 요소를 더한 값을 변수 answer에 저장
    answer = sum(list(map(int,str(n))))
    return answer