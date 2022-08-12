def solution(clothes):
    # 옷의 종류를 기준으로 정렬
    clothes.sort(key=lambda x:x[1])
    
    clothes_sort = [] # 옷의 종류를 담을 리스트
    for i in clothes:
        # 아직 담지 않은 옷의 종류를 추가(set로 할 걸)
        if not i[1] in clothes_sort:
            clothes_sort.append(i[1])
    
    # 옷의 종류를 key, 인덱스를 value로 딕셔너리 생성
    clothes_sort = {clothes_sort[x]:x for x in range(len(clothes_sort))}
    # 실제 옷이 담길 리스트
    closet = [[] for _ in range(len(clothes_sort))]
    
    for cloth,sorting in clothes:
        # 옷의 종류를 키로 삼아 이중 리스트 내에 옷을 추가
        closet[clothes_sort[sorting]].append(cloth)
    
    # 옷의 개수를 종류별로 담을 리스트
    counting = []
    for i in closet:
        counting.append(len(i))
    
    # 옷의 종류가 한 개면 옷의 개수 그대로 출력
    if len(counting) == 1:
        return counting[0]
    else: # 옷의 종류가 여러 개면
        total = 0 # 최종 결과
        temp = 1 # 임시 변수
        for i in counting:
            temp *= (i+1)
        total += temp - 1
        return total