def solution(id_list, report, k):
    # 정답 리스트 초기화(보고 결과)
    answer = [0] * len(id_list)   
    # 신고 당한 횟수 리스트 
    reports = {x : 0 for x in id_list}

    for r in set(report):
        # 신고 당한 사람
        reports[r.split()[1]] += 1

    for r in set(report):
        # k번 이상 신고를 당했으면
        if reports[r.split()[1]] >= k:
            # 신고한 사람의 인덱스로 접근해 +1
            answer[id_list.index(r.split()[0])] += 1

    return answer