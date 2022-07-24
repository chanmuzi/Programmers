def solution(participant, completion):
    # 참여자:0 으로 딕셔너리 생성
    check_dict = {x:0 for x in participant}
    # 참여자 명단에 있으면 딕셔너리 value 증가
    for i in participant:
        check_dict[i] += 1
    # 완주 명단에 있으면 딕셔너리 value 감소
    for i in completion:
        check_dict[i] -= 1
    for i in check_dict:
        # value가 1인 key 반환
        if check_dict[i] == 1: return i