# fail

def solution(n, computers):
    def find(x):
        if x == parents[x]:
            return x
        return find(parents[x])
    
    def union(n,m):
        pn = find(n)
        pm = find(m)
        if pn>pm:
            parents[n] = pm
        elif pn<pm:
            parents[m] = pn
    
    
    parents = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1 and parents[i]!=parents[j]:
                union(i,j)
    print(parents)
    visited = set()
    count = 0
    for x in range(n):
        px = find(x)
        if px not in visited:
            visited.add(px)
            count+=1
    
    return count

print(solution(4,[[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))
# 1
