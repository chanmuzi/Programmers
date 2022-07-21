def solution(arr):
    # 리스트 최솟값 제거
    arr.remove(min(arr))
    # 리스트 요소가 0개면 [-1] 반환
    if len(arr) == 0: return [-1]
    # 리스트 요소가 있으면 리스트 반환
    else: return arr