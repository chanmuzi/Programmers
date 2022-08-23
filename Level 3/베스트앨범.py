def solution(genres, plays):
    genres_count = dict() # 장르별 누적 재생수
    genres_idx = dict() # 장르별 인덱스 및 재생수
    
    for idx,genre in enumerate(genres):
        
        if genre not in genres_count: # 처음 확인하는 장르인 경우
            genres_count[genre] = plays[idx] # 재생수를 추가
            genres_idx[genre] = [(idx,plays[idx])] # 인덱스, 재생수를 추가
        else: # 기존에 확인했던 장르인 경우
            genres_count[genre] += plays[idx] # 재생수 더하기
            genres_idx[genre].append((idx,plays[idx])) # 인덱스, 재생수 추가
    
    # 장르 이름만 모아서 재생수를 기준으로 내림차순
    count_list = [x for x in genres_count]
    count_list.sort(key=lambda x:genres_count[x],reverse=True)
    
    answer = [] # 최종 결과 리스트
    for genre in count_list: # 장르별로
        temp = genres_idx[genre] # 인덱스와 재생수를 불러오기
        temp.sort(key=lambda x: x[1],reverse=True) # 재생수 기준 내림차순
        for i in range(2): # 최대 2곡 뽑기
            if temp: # 리스트가 비어있지 않다면
                answer.append(temp.pop(0)[0]) # 가장 왼쪽의 인덱스 뽑아오기
    
    return answer