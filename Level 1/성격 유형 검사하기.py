def solution(survey, choices):
    index_dict = {'R':0, 'T':0, 'C':0, 'F':0,
                  'J':0, 'M':0, 'A':0, 'N':0}
    
    for i in range(len(survey)):
        if choices[i] == 1:
            index_dict[survey[i][0]] += 3
        elif choices[i] == 2:
            index_dict[survey[i][0]] += 2
        elif choices[i] == 3:
            index_dict[survey[i][0]] += 1
        elif choices[i] == 4:
            continue
        elif choices[i] == 5:
            index_dict[survey[i][1]] += 1
        elif choices[i] == 6:
            index_dict[survey[i][1]] += 2
        elif choices[i] == 7:
            index_dict[survey[i][1]] += 3
            
    answer = ''
    if index_dict['R'] >= index_dict['T']:
        answer += 'R'
    else: answer += 'T'
    if index_dict['C'] >= index_dict['F']:
        answer += 'C'
    else: answer += 'F'
    if index_dict['J'] >= index_dict['M']:
        answer += 'J'
    else: answer += 'M'
    if index_dict['A'] >= index_dict['N']:
        answer += 'A'
    else: answer += 'N'
    
    return answer