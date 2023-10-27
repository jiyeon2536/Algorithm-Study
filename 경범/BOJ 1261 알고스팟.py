import heapq
import pprint

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
# 메인 로직

def sor(start):
    queue = []
    distance[0][0] = 0
    heapq.heappush(queue, start)
    while queue:
        a, b = heapq.heappop(queue)

        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if mat[ni][nj] == 1:
                    if distance[a][b] +1 < distance[ni][nj]:
                        distance[ni][nj] = distance[a][b] + 1
                        heapq.heappush(queue, [ni, nj])

                else:
                    if distance[a][b] < distance[ni][nj]:
                        distance[ni][nj] = distance[a][b]
                        heapq.heappush(queue, [ni, nj])





# 인풋

m, n = map(int, input().split())
mat = [list(map(int, input())) for _ in range(n)]
distance = [[1e9] * m for _ in range(n)]
start = [0, 0]


# 아웃풋
sor(start)
print(distance[n-1][m-1])
