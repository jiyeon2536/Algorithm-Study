import sys
sys.setrecursionlimit(10 ** 7)

n = int(input()) # 노드의 개수

# 부모 노드 리스트 생성
par = [0] * (n+1)

# 인접리스트 생성
lst = [[] for _ in range(n+1)]

# 간선 정보 입력
for _ in range(n-1):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
cnt = 0
# i값이 0이 아닌 경우 부모 노드 입력
def func(x):
    global cnt
    cnt += 1
    for i in lst[x]:
        if par[i] == 0:
            par[i] = x
            func(i)

func(1)

for i in par[2:]:
    print(i)
print(cnt)
