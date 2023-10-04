import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def village(start):
    visited[start] = True
    for i in tree[start]:
        if not visited[i]:
            village(i)
            # start 마을을 우수마을로 선택했을 경우
            dp[start][1] += dp[i][0]
            # start를 우수마을로 선택하지 않았을 경우
            dp[start][0] += max(dp[i][0], dp[i][1])

N = int(input())
population = [0] + list(map(int, input().split()))
# 마을간 연결 정보
tree = [[] for i in range(N+1)]
visited = [0 for i in range(N+1)]
dp = [[0, population[i]] for i in range(N+1)]
for i in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)
# 1번부터 출발
village(1)
# 1번 마을을 우수 마을로 선택했을 때와 선택하지 않았을 때 중 큰 값을 출력
print(max(dp[1][0], dp[1][1]))