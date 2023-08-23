from collections import deque
def bfs(n, k, cnt):
    que = deque([[n, cnt]])

    while que:
        n, cnt = que.popleft()
        # 숫자를 찾으면 카운트 리턴
        if n == k:
            return cnt
        # 연산 한 번 진핼 할 때마다 1 더해주기
        cnt += 1
        # 연산할 값이 범위내에 존재하는지
        # + 1과 * 2의 경우에는 숫자가 더 작아질 일이 없으므로 n이 K보다 큰 경우 제외
        # 연산할 값이 이전에 연산한 적이 없다면!
        if 0 <= n+1 <= 100000 and n <= k and visited[n + 1] == 0:
            que.append([n + 1, cnt])
            visited[n + 1] = 1
        if 0 <= n*2 <= 100000 and n <= k and visited[n * 2] == 0:
            que.append([n * 2, cnt])
            visited[n * 2] = 1
        if 0 <= n-1 <= 100000 and visited[n - 1] == 0:
            que.append([n - 1, cnt])
            visited[n - 1] = 1

n, k = map(int, input().split())
# 방문 체크열 생성
visited = [0] * 100001
print(bfs(n, k, 0))
