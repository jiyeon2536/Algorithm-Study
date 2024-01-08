def solution(rows, columns, queries):
    from pprint import pprint
    answer = []
    maps = [[0] * columns for _ in range(rows)]
    a = 1
    for i in range(rows):
        for j in range(columns):
            maps[i][j] = a
            a += 1
    for query in queries:
        x1, y1, x2, y2 = query[0], query[1], query[2], query[3]
        # 첫 시작값을 mn으로 지정
        mn = maps[x1 - 1][y1 - 1]
        nxt = maps[x1 - 1][y1 - 1]
        # 1: x1 고정, y 증가 (y1 -> y2) 
        i =  x1 - 1
        for j in range(y1, y2):
            nxt, maps[i][j] = maps[i][j], nxt
            mn =  min(mn, nxt)
            # print(nxt)
        # 2: y2 고정, x 증가 (x1 -> x2) 
        j =  y2 - 1
        for i in range(x1, x2):
            nxt, maps[i][j] = maps[i][j], nxt
            mn =  min(mn, nxt)
            # print(nxt)
        # 3: x2 고정, y 감소 (y2 -> y1)
        i =  x2 - 1
        for j in range(y2 - 2, y1 - 2, -1):
            nxt, maps[i][j] = maps[i][j], nxt
            mn =  min(mn, nxt)
            # print(nxt)
        # 4: y1 고정, x 감소 (x2 -> x1)
        j =  y1 - 1
        for i in range(x2 - 2, x1 - 2, -1):
            nxt, maps[i][j] = maps[i][j], nxt
            mn =  min(mn, nxt)
            # print(nxt)
        answer.append(mn)
    return answer
