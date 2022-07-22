def solution(price, money, count):
    # 필요한 돈 계산: price를 1부터 count까지 곱해 더한 값
    need_money = sum([x*price for x in range(1,count+1)])
    # 필요한 돈이 더 크다면 money를 빼서 반환, 그렇지 않으면 0 반환
    return need_money - money if need_money > money else 0