def solution(A,B):
    return sum([x*y for x,y in zip(sorted(A),reversed(sorted(B)))])