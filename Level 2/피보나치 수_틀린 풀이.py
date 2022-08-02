def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-2) + fibo(x-1)

def solution(n):
    temp = fibo(n)
    return temp % 1234567