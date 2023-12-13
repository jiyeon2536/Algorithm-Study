def solution(places):
    answer = []
    for place in places:
        # 조건 충족하는지 확인하는 변수
        condition = True
        # 대기실을 순회하면서 대기자가 있는지 확인
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    # 대기자의 주변 탐색
                    # 상하좌우 : 여기는 존재하면 무조건 충족 X
                    for di, dj in [[-1, 0], [1, 0], [0,-1], [0, 1]]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] == "P":
                            condition = False
                            break
                    if not condition:
                        break
                    
                    # 가림막 1개면 가능
                    for di, dj in [[-2, 0], [2, 0], [0,-2], [0, 2]]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] == "P":
                            if di == -2:
                                if place[i-1][j] != "X":
                                    condition = False
                                    break
                            elif di == 2:
                                if place[i+1][j] != "X":
                                    condition = False
                                    break
                            elif dj == -2:
                                if place[i][j-1] != "X":
                                    condition = False
                                    break
                            elif dj == 2:
                                if place[i][j+1] != "X":
                                    condition = False
                                    break
                    if not condition:
                        break
                    # 가림막 2개면 가능
                    for di, dj in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] == "P":
                            if place[ni][j] == "X" and place[i][nj] == "X":
                                pass
                            else:
                                condition = False
                                break
                    if not condition:
                        break
                if not condition:
                    break
        answer.append(int(condition))
    return answer
