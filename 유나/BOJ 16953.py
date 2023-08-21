def bfs(a, b):
    global visited
    que = []            # 빈 큐 생성
    que.append([a, 0])  # 몇번의 연산이 필요한지 체크하기 위하여 [val, cnt]
    while que:
        val, cnt = que.pop(0)
        if val == b: # 목표 값에 도달하면 멈추기
            break
        if val * 2 <= b or val * 10 + 1 <= b: # 둘 중에 하나에 걸리면 들어오세요
            if val * 2 <= b:
                que.append([val * 2, cnt + 1]) # 큐에 삽입
                visited.append([val * 2, cnt + 1]) # visited에 삽입

            if val * 10 + 1 <= b:
                que.append([val * 10 + 1, cnt + 1])
                visited.append([val * 10 + 1, cnt + 1])



a, b = map(int, input().split())
# 방문 체크 생성 : 처음엔 크기만큼 만들어줬는데 메모리초과로 빈 리스트로 생성함
visited = []
bfs(a, b)

# ans 초기값 설정
ans = -1
# 방문체크열을 돌면서 목표값이 존재하는 경우에는 cnt
# 존재하지 않은 경우에는 -1
for i in range(len(visited)):
    if visited[i][0] == b and visited[i][1] > 0:
        ans = visited[i][1] + 1
        break
    else:
        ans = -1

print(ans)
