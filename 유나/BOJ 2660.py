import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip()) # 회원의 수
# 인접 리스트 생성
graph = [[] for _ in range(n+1)]
while True:
    # 두 회원이 친구이다!
    u, v = map(int, input().strip().split())

    # -1, -1이면 입력 종료
    if u == v == -1:
        break
      
    # 왕복 가능하므로 u에서 v, v에서 u
    graph[u].append(v)
    graph[v].append(u)

# 회원 번호가 1부터 시작하므로 n+1만큼 점수표 생성
# 0번째 값에 가능한 최대 값 보다 큰 51점 입력
check = [51] + [0] * (n)

# 모든 노드를 시작점으로
for i in range(1, n+1):
    cnt = 1
    visited = [0] * (n+1)
    que = deque()
    que.append(i)
    visited[i] = 1
    # bfs
    while que:
        node = que.popleft()
        # 노드에서 갈 수 있는 만큼 돌면서
        for j in graph[node]:
            if visited[j] == 0:
                visited[j] += visited[node] + 1
                que.append(j)
                cnt += 1
              
  # 모든 회원과 만났다면, 방문 체크열의 최대 값으로 점수 입력
  if cnt == n:
        check[i] = max(visited)

# 회장 후보 점수
# 방문 체크열 돌 때 시작점 1도 더해졌으므로 1 빼줌
mn = min(check) - 1
# 회장 후보 리스트
# 후보 점수 가진 사람 append
res = []
for idx in range(1, n+1):
    if check[idx] - 1 == mn:
        res.append(idx)

print(mn, len(res))
print(*sorted(res))
