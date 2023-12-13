import sys
input = sys.stdin.readline
from collections import deque

# BFS
def is_vaild(election):
    tmp = deque()
    union = [0] * (N+1)
    tmp.append(election[0])
    union[election[0]] = True
    cnt = 1
    result = 0
    while tmp:
        s = tmp.popleft()
        result += population[s]
        for i in nodes[s]:
            if i in election and not union[i]:
                union[i] = True
                cnt += 1
                tmp.append(i)
    if cnt == len(election):
        return result
    else:
        return 0

# DFS
def Binding(cnt, s, boundary):
    global mn
    if cnt == boundary:
        election_1 = deque()
        election_2 = deque()
        for i in range(1, N+1):
            if visited[i]:
                election_1.append(i)
            else:
                election_2.append(i)
        is_vaild_election_1, is_vaild_election_2 = is_vaild(election_1), is_vaild(election_2)
        if is_vaild_election_1 and is_vaild_election_2:
            mn = min(mn, abs(is_vaild_election_1 - is_vaild_election_2))
            return
        else:
            return
    else:
        for i in range(s, N + 1):
            if not visited[i]:
                visited[i] = 1
                Binding(cnt+1, i, boundary)
                visited[i] = 0

N = int(input())
population = [0] + list(map(int, input().split()))
nodes = [[]]
for _ in range(N):
    nodes.append(list(map(int, input().split()))[1:])

mn = 1000
for i in range(1, N//2+1):
    visited = [0] * (N+1)
    Binding(0, 1, i)

if mn == 1000:
    print(-1)
else:
    print(mn)