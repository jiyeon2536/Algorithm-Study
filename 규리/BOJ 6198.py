N = int(input())  # 빌딩 개수
building = [int(input()) for _ in range(N)]
cnt = [0]*N  # i번째 빌딩옥상 확인할 수 있는 관리인 수
stack = []
for i in range(N):
    while stack:
        # i번째 빌딩 건물보다 낮으면 i번째 빌딩 오른쪽을 볼 수 없음
        if stack[-1] > building[i]:
            break
        stack.pop()
    cnt[i] = len(stack)
    # stack: i번째 빌딩옥상을 확인할 수 있는 관리인의 빌딩 높이 (내림차순으로 담겨있음)
    stack.append(building[i])
print(sum(cnt))
