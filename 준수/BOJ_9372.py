T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    for _ in range(M):
        a, b = map(int, input().split())

    # 모든 노드는 이어져 있고 N-1가지의 비행기만 타면 목적지에 갈 수 있음
    print(N - 1)