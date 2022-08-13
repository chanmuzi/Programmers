def solution(n, left, right):
    share_left,idx_left = divmod(left,n)
    share_right,idx_right = divmod(right,n)

    answer = []
    left_list = []
    for i in range(n):
        if i <= share_left:
            left_list.append(share_left+1)
        else: left_list.append(i+1)
    left_list = left_list[idx_left:]
    for i in left_list:
        answer.append(i) 
    
    for i in range(share_left+1,share_right):
        for j in range(n):
            if j <= i: answer.append(i+1)
            else: answer.append(j+1)
        
    right_list = []
    for i in range(n):
        if i <= share_right:
            right_list.append(share_right+1)
        else: right_list.append(i+1)
    right_list = right_list[:idx_right+1]
    for i in right_list:
        answer.append(i)

    return answer