def solution(nums):
    # 중복을 제거한 세트의 길이가 뽑을 숫자보다 크거나 같으면 뽑을 숫자 반환
    # 그렇지 않다면 세트의 길이를 반환
    return len(nums)//2 if len(set(nums)) >= len(nums)//2 else len(set(nums))