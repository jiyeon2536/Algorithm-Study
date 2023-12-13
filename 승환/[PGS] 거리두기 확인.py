def solution(places):
    answer = []
    # 맨허튼 거리 2 안에 탐색하기 --> 완탐,,,? or 범위를 미리 지정
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 2. 파티션이 없는 경우... -> 해당위치에서 사방탐색해서 응시자가 없으면 넘어간다
    def chk2(place, x, y, nx, ny):
        for k in range(4):
            nnx = nx + dx[k]
            nny = ny + dy[k]
            if 0 <= nnx < 5 and 0 <= nny < 5:
                # 사방탐색 중 처음 시작한 사람 자리는 탐색하지 않는다.
                if nnx == x and nny == y:
                    continue
                # 맨허튼 거리 2에 사람이 있을 경우..
                if places[place][nnx][nny] == 'P':
                    # True 반환해서 True일 경우 0반환
                    return True
        return False

    # 1. 사방탐색 해서 파티션이있으면 상관없다.
    def chk(place, x, y):
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 범위 안에 있을 경우
            if 0 <= nx < 5 and 0 <= ny < 5:
                # 사람인경우 False
                if places[place][nx][ny] == 'P':
                    return False
                # 파티션으로 막아놓으면 성공
                elif places[place][nx][ny] == 'X':
                    continue
                # 파티션 없는 경우
                elif places[place][nx][ny] == 'O':
                    # 해당 위치에서 사방탐색 한다.
                    if chk2(place, x, y, nx, ny):
                        return False    
        # 포문 도는동안 return 없으면 맨허튼 거리 2안에 사람 X
        return True

    num = 1
    for place in range(5):
        for i in range(5):
            # answer가 place보다 커지면 중간에 거리두기에 실패한 것.
            if len(answer) > place:
                break
            for j in range(5):
                # 한 줄에 실패를 두번 할 수도 있다.
                if len(answer) > place:
                    break
                if places[place][i][j] == 'P':
                    # 사람인 경우에만 체크
                    if chk(place, i, j):
                        pass
                    else:
                        answer.append(0)
                        break
        # for문 다 돌았는데 답 크기가 작으면 거리두기 성공한 것 
        if len(answer) <= place:
            answer.append(1)
    return answer
