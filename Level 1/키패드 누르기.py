def solution(numbers, hand):
    # 숫자패드 딕셔너리 생성, (x,y) 형태
    num_pad = {1:[0,0], 2:[0,1],3:[0,2],
               4:[1,0],5:[1,1],6:[1,2],
               7:[2,0],8:[2,1],9:[2,2],
               '*':[3,0],0:[3,1],'#':[3,2]}
    
    # 왼손 위치
    left_position = num_pad['*']
    # 오른손 위치
    right_position = num_pad['#']
    # 손 순서 리스트
    which_hand = []

    # 방향 리스트 각 원소에 대해
    for i in numbers:
        # 찾아갈 번호 위치 받아오기
        i_position = num_pad[i]
        # 1,4,7이면 왼손
        if i in [1,4,7]:
            which_hand.append('L')
            left_position = i_position
        # 3,6,9이면 오른손
        elif i in [3,6,9]:
            which_hand.append('R')
            right_position = i_position
        # 나머지이면 가까운 손    
        else:
            # 왼손과 목표까지의 거리                
            left_distance = (abs(i_position[0]-left_position[0])
                             +abs(i_position[1]-left_position[1]))
            # 오른손과 목표까지의 거리
            right_distance = (abs(i_position[0]-right_position[0])
                              +abs(i_position[1]-right_position[1]))
            # 왼손까지의 거리가 더 짧으면 왼손 적용
            if left_distance < right_distance:
                which_hand.append('L')
                left_position = i_position
            # 오른손까지의 거리가 더 짧으면 오른손 적용
            elif left_distance > right_distance:
                which_hand.append('R')
                right_position = i_position
            # 거리가 동일하면
            else:
                # hand의 정보를 받아 오른손 혹은 왼손 적용
                if hand == 'right':
                    which_hand.append('R')
                    right_position = i_position
                else:
                    which_hand.append('L')
                    left_position = i_position
    
    # 문자열로 변환하여 반환                
    return ''.join(which_hand)
        