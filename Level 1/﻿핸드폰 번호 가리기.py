def solution(phone_number):
    # 문자열을 리스트로 변경
    my_list = list(phone_number)
    # 오른쪽에서 네번째까지 *로 변경
    my_list[:-4] = '*'*(len(phone_number)-4)
    # 리스트를 문자열로 변경
    answer = ''.join(my_list)
    return answer