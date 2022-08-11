def solution(people, limit):
    # 오름차순 정렬
    people.sort()
    start = 0
    end = len(people) - 1
    cnt = 0
    
    # 시작값이 끝값 이하
    while start <= end:
        # 둘을 더한 값이 범위 내라면 한 칸씩 땡기기
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        # 둘을 더한 값이 범위 밖이면 뒷 사람만 땡기기
        else: end -= 1
        # 보트 수 증가
        cnt += 1
    
    return cnt