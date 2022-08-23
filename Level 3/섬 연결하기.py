def solution(n, costs):
    # 부모 노드 찾기
    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]
    
    # 부모 노드 합치기
    def union_parent(a,b):
        a = find_parent(a)
        b = find_parent(b)
        
        if a < b:
            parent[b] = a
        else: parent[a] = b
    
    # 부모 노드, 간선, 최종 결과 초기화
    parent = [x for x in range(n+1)]
    edges = []
    result = 0
    
    # 시작,도착,비용
    for a,b,cost in costs:
        edges.append((cost,a,b))
    
    # 오름차순 정렬
    edges.sort()
    
    for cost,a,b in edges:
        # 아직 연결되지 않은 노드들만 합치기
        if find_parent(a) != find_parent(b):
            union_parent(a,b)
            result += cost
        
    return result