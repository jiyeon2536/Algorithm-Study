import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def f(x):
    for i in tree[x]:
        if visited[i] == False:
            visited[i] = True
            P[i] = x
            f(i)

N = int(input())
tree = [[] for _ in range(N+1)]
P = [0] * (N+1)  # 부모 저장
visited = [False for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited[1] = True
f(1)
for i in range(2, N+1):
    print(P[i])
