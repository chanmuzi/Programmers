def solution(board, moves):
    # 뽑은 인형이 들어갈 리스트
    basket = []
    # 터진 인형의 개수
    count = 0
    
    # 각 이동에 대해
    for i in moves:
        # n만큼 반복, 맨 윗줄부터 조사
        for j in range(len(board)):
            # 0이 아닌, 즉 인형이 있는 칸을 만나면
            if board[j][i-1] != 0:
                # 바구니가 비어있을 경우
                if len(basket) == 0:
                    # 바구니에 그냥 추가하고 뽑은 인형은 비워주기
                    basket.append(board[j][i-1])
                    board[j][i-1] = 0
                    # 다음 moves로 넘어가기
                    break
                # 바구니의 마지막 인형과 새로 넣을 인형이 같으면
                elif basket[-1] == board[j][i-1]:
                    # 바구니 마지막 인형 제거
                    basket.pop()
                    # 뽑은 인형은 비워주고 count
                    board[j][i-1] = 0
                    count += 2
                    # 다음 moves로 넘어가기
                    break
                # 바구니에 넣을 인형과 바구니의 마지막 인형이 같지 않으면
                else:                   
                    # 바구니에 새 인형 넣기
                    basket.append(board[j][i-1])
                    # 뽑은 인형 비워주기
                    board[j][i-1] = 0
                    # 다음 moves로 넘어가기
                    break
    return count