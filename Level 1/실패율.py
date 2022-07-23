# Counter 클래스 불러오기
from collections import Counter
def solution(N, stages):
    # 스테이지별 개수 딕셔너리로 저장
    show_count = Counter(stages)
    # 리스트 0으로 초기화
    initial_list = [0]*(N+1)
    
    # N+1번째까지 반복
    for i in range(1,N+2):
        # 딕셔너리에 존재하면 초기 리스트에 갱신, 없는 스테이지는 0으로 유지
        if show_count[i]: initial_list[i-1] = show_count[i]
    
    # 실패율 리스트 초기화    
    fail_list = []
    # 전체 인원 수
    total_users = len(stages)
    # 현재 스테이지 전까지 도전한 사람 수
    current_stage_users = 0
    # 0부터 N-1까지
    for i in range(N):
        # 실패율 = 현재 스테이지 도전 수/(전체-직전까지 도전 수), 분모가 0이 아닐때는 나눗셈, 분모가 0이면 0으로 취급
        failure = initial_list[i]/(total_users-current_stage_users) if (total_users-current_stage_users) else 0
        # 직전까지 도전 수 추가
        current_stage_users += initial_list[i]
        # 실패 리스트에 실패율과 스테이지 번호를 리스트로 추가
        fail_list.append([failure,i+1])
    
    # 실패율 리스트 정렬
    fail_list.sort()
    # 실패율 기준 내림차순, 스테이지 번호 기준 오름차순
    fail_list.sort(key=lambda x:(-x[0],x[1]))        
    
    # 정답 리스트는 실패율 리스트의 두 번째 요소(스테이지 번호)의 모음
    answer = [x[1] for x in fail_list]
    return answer