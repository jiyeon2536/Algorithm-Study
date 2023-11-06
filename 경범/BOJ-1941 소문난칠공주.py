from itertools import combinations
from collections import deque
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 메인 로직


def sor(start, arr):

    queue = deque()
    vis = [False] * 7
    queue.append(start)
    vis[0] = True
    while queue:

        a, b = queue.popleft()
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if (ni, nj) in arr:
                i = arr.index((ni, nj))
                if vis[i] == True:
                    continue
                else:
                    vis[i] = True
                    queue.append((ni,nj))
    if False in vis:
        return False
    else:
        return True


# 인풋
mat = [list(input()) for _ in range(5)]

total = 0
arr = []

for i in range(5):
    for j in range(5):
        arr.append((i,j))

arr7 = list(combinations(arr, 7))

for i in arr7:
    start = (i[0][0], i[0][1])
    rs = sor(start, i)
    if rs == True:
        cnt = 0
        for j in i:
            a, b = j
            if mat[a][b] == 'S':
                cnt += 1
        if cnt >= 4:
            total += 1





# 아웃풋
print(total)



