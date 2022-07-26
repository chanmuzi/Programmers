def solution(id_list, report, k):
    # 최종 정답 리스트
    answer_list = []
    
    # 신고당한 수 리스트
    report_list = [0]*len(id_list)
    # 입력 순서대로 id 딕셔너리 생성
    id_dict = {id_list[i]:i for i in range(len(id_list))}
    
    # 신고하는 사람이 누굴 신고했는지 담을 리스트
    reporting_list = [[] for i in range(len(id_list))]
    # 중복 제거
    report = list(set(report))
    for i in report:
        # 신고자, 신고받은 사람 나누기
        reporter, reported = i.split()
        # 누굴 신고했는지 추가
        reporting_list[id_dict[reporter]].append(reported)
        # 신고 당한 횟수 증가
        report_list[id_dict[reported]] += 1
    
    # k를 넘는지 확인할 리스트    
    pass_list = []
    for i in report_list:
        # k 미만이면 True
        if i < k: pass_list.append(True)
        # k 이상이면 False
        else: pass_list.append(False)
    
    # 누굴 신고했는지에 대한 리스트에서
    for i in reporting_list:
        temp = 0
        for j in range(len(i)):
            # 신고당한 사람이 True이면 패스
            if pass_list[id_dict[i[j]]]: continue
            # 신고당한 사람이 False이면 temp 증가
            else: temp += 1
        # temp만큼 최종 결과 리스트에 추가
        answer_list.append(temp)
    
    return answer_list