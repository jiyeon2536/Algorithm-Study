def make_set(N):
    parent = [i for i in range(N+1)]
    return parent

def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])

def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px != py:
        parent[px] = py

N = int(input())  # 도시의 수
M = int(input())  # 여행 계획에 속한 도시들의 수
parent = make_set(N)  # 초기화하는 과정

box = [list(map(int, input().split())) for _ in range(N)]
M_list = list(map(int ,input().split()))  # 여행 계획

for i in range(N):
    for j in range(N):
        if box[i][j] == 1:
            union((i+1), (j+1))

check = True
find = find_set(M_list[0])

for m in M_list:
    if find != find_set(m):
        check = False
        break

if check == True:
    print('YES')
else:
    print('NO')
