# 날짜 모듈 불러오기
import datetime
def solution(a, b):
    # 2016년 a월 b일 정보를 변수 date에 저장
    date = datetime.date(2016,a,b)
    # 요일별로 딕셔너리 생성, key값을 숫자로 설정
    my_dict = {0:'MON',1:'TUE',2:'WED',3:'THU',4:'FRI',5:'SAT',6:'SUN'}
    # 함수를 통해 반환 받은 숫자를 key로 사용
    return my_dict[date.weekday()]