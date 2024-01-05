def solution(maps):
    answer = []
    # 사방탐색으로 이어진거 확인해서 넣으면 끝
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    def chk(x, y):
        nonlocal answer
        q = [(x, y)]
        temp = 0
        while q:
            x, y = q.pop(0)
            # print(maps[x][y])
            temp += int(maps[x][y])
            maps[x][y] = "X"
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < len(maps) and 0 <= ny < long and maps[nx][ny] != 'X' and (nx, ny) not in q:
                    q.append((nx, ny))
        answer.append(temp)
    for map in range(len(maps)):
        maps[map] = list(maps[map])
        long = len(maps[map])
    for map in range(len(maps)):
        for j in range(len(maps[map])):
            if maps[map][j] != 'X':
                chk(map, j)
    if answer:
        answer.sort()
    else:
        answer.append(-1)
    return answer
