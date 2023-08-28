import pprint

for tc in range(1, 11):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # arr 의 세로줄만 보면서 1 아래에 0 뿐이라면 1과 0의 위치를 바꿔나간다 (아래로 떨어짐)
    # 마찬가지로 2 위에 아무것도 없댜면 0과 2의 위치를 바꿈 (아래로 떨어짐)
    # while 돌면서 더 이상 이동이 없을 때까지, 1 의 아래가 0이라면 아래칸으로 이동, (1 <-> 0)
    # 2 의 위가 0이라면 위칸으로 이동, (2 <-> 0)

    for j in range(N):
        i = 0
        while i < N - 2:
            if arr[i][j] == 1 and arr[i + 1][j] == 0:
                arr[i][j], arr[i + 1][j] = 0, 1
                i += 1
            if arr[N - 1][j] == 1:
                arr[N - 1][j] = 0

            if arr[i][j] == 0 and arr[i + 1][j] == 2:
                arr[i + 1][j], arr[i][j] = 0, 2
                i += 1
            if arr[0][j] == 2:
                arr[0][j] = 0

            else:
                i += 1
    pprint.pprint(arr)


'''
7
1 0 2 0 1 0 1
0 2 0 0 0 0 0
0 0 1 0 0 1 0
0 0 0 0 1 2 2
0 0 0 0 0 0 0
0 0 2 1 0 2 1
0 0 1 2 2 0 2
'''