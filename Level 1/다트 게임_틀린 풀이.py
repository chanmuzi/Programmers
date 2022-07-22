def solution(dartResult):
    dartResult = list(dartResult)
    list_1 = []
    list_2 = []
    list_3 = []
    for i in range(len(dartResult)):
        if dartResult[i].isdigit() and len(list_1)==0: list_1.append(dartResult[i])
        elif dartResult[i].isdigit() and len(list_2)==0: list_2.append(dartResult[i])
        elif dartResult[i].isdigit(): list_3.append(dartResult[i])
        elif dartResult[i].isalpha() and len(list_1)==1: list_1.append(dartResult[i])
        elif dartResult[i].isalpha() and len(list_2)==1: list_2.append(dartResult[i])
        elif dartResult[i].isalpha(): list_3.append(dartResult[i])
        elif (dartResult[i] == '*' or dartResult[i] == '#') and len(list_2) == 0: list_1.append(dartResult[i])
        elif (dartResult[i] == '*' or dartResult[i] == '#') and len(list_3) == 0: list_2.append(dartResult[i])
        elif (dartResult[i] == '*' or dartResult[i] == '#'): list_3.append(dartResult[i])
    if '1' in list_1 and '0' in list_1:
        length = len(list_1)
        temp = list_1[:]
        list_1 = ['10']
        if length == 3: list_1.append(temp[2])
        else: list_1.append(temp[3])
    if '1' in list_2 and '0' in list_2:
        length = len(list_2)
        temp = list_2[:]
        list_2 = ['10']
        if length == 3: list_2.append(temp[2])
        else: list_2.append(temp[3])        
    if '1' in list_3 and '0' in list_3:
        length = len(list_3)
        temp = list_3[:]
        list_3 = ['10']
        if length == 3: list_3.append(temp[2])
        else: list_3.append(temp[3])        
        
    if list_1[1] == 'S': num1 = int(list_1[0])
    elif list_1[1] == 'D': num1 = int(list_1[0])*int(list_1[0])
    else: num1 = list_1[0]*int(list_1[0])*int(list_1[0])
    
    if list_2[1] == 'S': num2 = int(list_2[0])
    elif list_2[1] == 'D': num2 = int(list_2[0])*int(list_2[0])
    else: num2 = int(list_2[0])*int(list_2[0])*int(list_2[0])
    
    if list_3[1] == 'S': num3 = int(list_3[0])
    elif list_3[1] == 'D': num3 = int(list_3[0])*int(list_3[0])
    else: num3 = int(list_3[0])*int(list_3[0])*int(list_3[0])
        
    if '#' in list_1:
        num1 = (-num1)
        if '#' in list_2:
            num2 = (-num2)
            if '#' in list_3: num3 = (-num3)
            elif '*' in list_3:
                num2 *= 2
                num3 *= 2
        elif '*' in list_2:
            num1 *= 2
            num2 *= 2
            if '#' in list_3: num3 = (-num3)
            elif '*' in list_3:
                num2 *= 2
                num3 *= 2
        else:
            if '#' in list_3: num3 = (-num3)
            elif '*' in list_3:
                num2 *= 2
                num3 *= 2
    elif '*' in list_1:
        num1 *= 2
        if '#' in list_2:
            num2 = (-num2)
            if '#' in list_3: num3 = (-num3)
            elif '*' in list_3:
                num2 *= 2
                num3 *= 2
        elif '*' in list_2:
            num1 *= 2
            num2 *= 2
            if '#' in list_3: num3 = (-num3)
            elif '*' in list_3:
                num2 *= 2
                num3 *= 2
        else:
            if '#' in list_3: num3 = (-num3)
            elif '*' in list_3:
                num2 *= 2
                num3 *= 2                
    else:
        if '#' in list_2:
            num2 = (-num2)
            if '#' in list_3: num3 = (-num3)
            elif '*' in list_3:
                num2 *= 2
                num3 *= 2
        elif '*' in list_2:
            num1 *= 2
            num2 *= 2
            if '#' in list_3: num3 = (-num3)
            elif '*' in list_3:
                num2 *= 2
                num3 *= 2
        else:
            if '#' in list_3: num3 = (-num3)
            elif '*' in list_3:
                num2 *= 2
                num3 *= 2                        
        
        
    answer = int(num1) + int(num2) + int(num3)
    return answer