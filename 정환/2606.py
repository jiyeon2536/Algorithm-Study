# DFS 함수 생성
def dfs(n, V, adj_m):
    global visited
    global result

    stack = []
    # 시작지점은 방문한 상태이므로 True 처리
    visited[n] = True
    while True:
        # 컴퓨터가 1번 부터 인덱싱 하므로 시작 범위는 1 부터 시작
        for w in range(1, V + 1):
            # 방문하고자 하는 경로에 길이 존재하고, 방문하지 않은 길이라면,
            if adj_m[n][w] == 1 and visited[w] == False:
                # 스택에 현재 정점을 push
                stack.append(n)
                # n 을 현재 정점으로 갱신
                n = w
                # 이어진 경로를 판단하는 result 리스트에 현재 정점 push
                result.append(n)
                # 현재 정점 방문표시
                visited[n] = True
                break
        # 현재 진행 방향에서 더 이상 진행할 경로가 존재하지 않을 경우,
        else:
            # 스택에 지나온 정점이 남아있다면
            if stack:
                # pop 을 통해 현재 위치를 남아있는 위치로 돌아가고 다른 방향의 경로를 탐색
                n = stack.pop()
            # 스택이 비어있다면 반복문 종료
            else:
                break
    return

# 컴퓨터의 수 ( 정점의 수 )
computers = int(input())

# 네트워크가 직접 연결되어 있는 컴퓨터 쌍의 수
pairs = int(input())

connect = []
# 방문 현황, 인덱싱이 0 부터 이루어지므로 1번부터 시작하는 문제에 대한
# 편의성을 높이기 위해 한 칸 더 생성한다
visited = [False] * (computers + 1)

# 네트워크로 연결되어 있는 정보를 입력으로 받아오면서 이차원 리스트화 시키기 위해
# 먼저 일차원 리스트에 담는다
for pair in range(pairs):
    connect.append(list(map(int, input().split())))

# 네트워크 간의 연결 현황을 표시하기 위한 이차원 리스트의 베이스 생성
adj = [[0] * (computers + 1) for _ in range(computers + 1)]

# 네트워크 연결을 담은 일차원 리스트를 순회하면서 이차원 리스트에 표시
# 연결 되어 있다면 1로 변경
for i in range(pairs):
    v1, v2 = connect[i][0], connect[i][1]
    adj[v1][v2] = 1
    adj[v2][v1] = 1

result = []

dfs(1, computers, adj)

print(len(result))