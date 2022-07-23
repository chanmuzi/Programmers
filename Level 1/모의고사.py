def solution(answers):
    # 반복 패턴 리스트로 생성
    list_1 = [1,2,3,4,5]
    list_2 = [2,1,2,3,2,4,2,5]
    list_3 = [3,3,1,1,2,2,4,4,5,5]
    
    # 제출한 정답을 문제 길이를 기준으로 리스트화
    answer_1 = list_1 * (len(answers)//5) + list_1[:len(answers)%5]
    answer_2 = list_2 * (len(answers)//8) + list_2[:len(answers)%8]
    answer_3 = list_3 * (len(answers)//10) + list_3[:len(answers)%10]
    
    # 정답 개수 리스트 초기화
    answer_count = [0,0,0]
    # 정답 리스트와 비교하여 같을 경우 정답 개수 추가
    for i in range(len(answers)):
        if answers[i] == answer_1[i]: answer_count[0] += 1
        if answers[i] == answer_2[i]: answer_count[1] += 1
        if answers[i] == answer_3[i]: answer_count[2] += 1
    
    # 점수의 최고값 변수에 저장
    high_score = max(answer_count)
    # 최고 점수 학생 리스트
    high_student = []
    for i in range(3):
        # 최고 점수를 받은 학생 번호를 리스트에 추가
        if answer_count[i] == high_score: high_student.append(i+1)
        
    return high_student