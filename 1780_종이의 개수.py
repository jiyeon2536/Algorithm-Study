import sys
input = sys.stdin.readline

def DFS(ix, iy, N):
    check = initial[ix][iy]
    # 전체 순회
    for y in range(iy, iy + N):
        for x in range(ix, ix + N):
            # 다른값이 나오면
            if initial[y][x] != check:
                # 9분할
                for i in range(3):
                    for j in range(3):
                        DFS(ix + i * N // 3, iy + j * N // 3, N // 3)
                # 다시 돌지 않도록 리턴
                return
    # 모두 같은 값일 경우
    if check == -1:
        result[0] += 1
    elif check == 0:
        result[1] += 1
    else:
        result[2] += 1

# 종이의 크기
N = int(input())
# 최초의 종이
initial = [list(map(int, input().split())) for _ in range(N)]
# -1, 0, 1 종이의 개수
result = [0, 0, 0]

DFS(0, 0, N)
for cnt in result:
    print(cnt)