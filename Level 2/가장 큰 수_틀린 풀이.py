def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x:(int(x[0]),int(x[-1])),reverse=True)
    return ''.join(numbers)