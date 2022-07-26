def solution(lottos, win_nums):
    # 일치 숫자 개수
    match = 0
    # 0이 아닌 숫자 개수
    except_zero = 0
    # 맞은 개수 : 순위
    rank_dict = {0:6,1:6,2:5,3:4,4:3,5:2,6:1}
    
    for i in lottos:
        # 숫자가 0이면 패스
        if i == 0: continue
        # 0이 아니면
        elif i != 0:
            # 0이 아닌 숫자 개수 +
            except_zero += 1
            # 당첨 번호에 들어있으면 일치 +
            if i in win_nums: match += 1
    
    # 0인 숫자가 하나도 없으면 
    if except_zero == len(lottos): return [rank_dict[match], rank_dict[match]]
    # 0인 숫자가 있으면
    else:
        # 0의 개수를 구하고
        zero = len(lottos)-except_zero
        # 딕셔너리 key에 추가하여 최댓값
        return[rank_dict[match+zero],rank_dict[match]]