# 백준 1135 뉴스 전하기

import sys
input = sys.stdin.readline

def solution(N,arr):
    dp = [0]*N
    graph =[[] for _ in range(N)]
    for i in range(1,N):
        graph[arr[i]].append(i)
    def dfs(v):
        stack = []
        for u in graph[v]:
            dfs(u)
            stack.append(dp[u])
        stack.sort(reverse=True)
        for i in range(len(stack)):
            dp[v] = max(dp[v], stack[i]+i+1)
        # print(v, dp[v])

    dfs(0)
    return dp[0]

N = int(input())
arr = list(map(int, input().split()))
print(solution(N,arr))
