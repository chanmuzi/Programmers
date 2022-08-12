from itertools import permutations
    
def solution(name):
    cases = permutations([x for x in range(len(name))])
    results = []
    for case in cases:
        cnt = 0
        
        moves = 0
        for j in range(len(case)-1):
            gap1 = max(case[j],case[j+1]) - min(case[j],case[j+1])
            gap2 = len(case)-max(case[j],case[j+1])+min(case[j],case[j+1])
            moves += min(gap1,gap2)
        cnt += moves
        
        for j in range(len(name)):
            if ord(name[j]) - ord('A') > 13:
                cnt += (91-ord(name[j]))
            else: cnt += ord(name[j]) - ord('A')
        
        results.append(cnt)
    return min(results)