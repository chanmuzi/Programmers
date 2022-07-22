def getDayName(a,b):
    # 월별로 일수 추가하기
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 1월 1일이 금요일이므로 이를 기준으로 설정
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    # 1월 1일부터 몇일이 지났는지 계산하여 나머지를 인덱스로 활용
    return days[(sum(months[:a-1])+b-1)%7]