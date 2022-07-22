def solution(arr):
    # 결과 리스트 초기화
    result_list = []
    # 첫 번째 요소 추가
    result_list.append(arr[0])
    # 기존 리스트의 마지막 요소까지
    for i in range(len(arr)-1):
        # 앞 요소와 뒤 요소가 같으면 무시
        if arr[i] == arr[i+1]: continue
        # 다르면 뒤 요소를 추가
        else: result_list.append(arr[i+1])
    # 결과 리스트 반환        
    return result_list