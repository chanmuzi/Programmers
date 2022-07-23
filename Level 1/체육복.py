def solution(n, lost, reserve):
    # lost에 없는 요소들을 전부 추가
    result_list = [x for x in range(1,n+1) if x not in lost]
    # reserve와 lost에 둘 다 있는 사람
    cross_list = list(set(reserve)&set(lost))
    for i in cross_list:
        # reserve와 lost에서 둘 다 제거
        reserve.remove(i)
        lost.remove(i)
        # 결과 리스트에 추가
        result_list.append(i)            
    
    # lost에 대해
    for i in sorted(lost):
        # 작은 것이 reserve에 있으면 
        if (i-1) in reserve:
            # 결과 리스트에 추가
            result_list.append(i)
            # 여분 리스트에서는 제거
            reserve.remove(i-1)
        # 작은 것은 없고 큰 숫자의 여분만 있으면    
        elif (i+1) in reserve:
            # 그것을 결과 리스트에 추가
            result_list.append(i)
            # 여분 리스트에서는 제거
            reserve.remove(i+1)
        # 해당 사항이 없으면 다른 사람으로 넘어가기
        else:continue          
    # 최종 결과 리스트에 있는 사람 수 반환
    answer = len(result_list)
    return answer