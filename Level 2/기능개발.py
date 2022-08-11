def solution(progresses, speeds):
    days = [] # 개발까지 걸리는 기간을 담을 리스트
    for progress,speed in zip(progresses,speeds):
        # 나머지가 0일 경우
        if (100-progress) % speed == 0:
            day = (100-progress) // speed
        # 나머지가 0이 아닐 경우
        else: day = (100-progress) // speed + 1
        # 계산된 기간을 리스트에 추가
        days.append(day)
        
    publish = [] # 배포당 개수를 담을 리스트
    stack = [days[0]] # 스택 초기화
    # 두 번째 항부터 마지막과 비교
    for i in range(1,len(days)):
        # 스택의 가장 큰 값이 비교값 이상이면 스택 추가
        if stack[0] >= days[i]:
            stack.append(days[i])
        # 스택의 가장 큰 값보다 작은 값이 나타나면
        else:
            # 스택의 길이를 배포 리스트에 추가하고 스택 초기화
            publish.append(len(stack))
            stack = [days[i]]
    # 마지막 남은 스택을 배포 리스트에 추가
    if stack:
        publish.append(len(stack))
    return publish
