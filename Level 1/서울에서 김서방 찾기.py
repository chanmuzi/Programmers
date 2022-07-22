def solution(seoul):
    # 김서방의 위치 저장
    index_kim = seoul.index('Kim')
    # f-string을 통해 문자열 저장
    answer = f'김서방은 {index_kim}에 있다'
    return answer