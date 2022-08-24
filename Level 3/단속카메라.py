def solution(routes):
    answer = 0
    # 진출 시점을 기준으로 정렬
    routes.sort(key=lambda x:x[1])
    cur = -30001 # 현재 카메라 설치 위치
    
    for route in routes:
        # 현재 카메라 이후에 진출하는 경우
        if cur < route[0]:
            answer += 1
            cur = route[1]
    return answer