def solution(plans):
    answer = []
    # 과제를 끝낸 순서대로 배열에 담는다.
    # 진행중인 과제가 있으면 멈춘다.
    # 과제를 끝낸 시각에 새로 시작해야하는 과제와 잠시 멈춰둔 과제가 있으면 새로 시작해야
    # 하는 과제부터 진행한다.
    # 시작 시간 기준으로 정렬한다.
    arr = sorted(plans, key=lambda x: x[1])
    hmwrk = []
    for i in range(len(arr) - 1):
        # 출발 시간 사이의 간격이 과제 걸리는 시간보다 커서 바로 끝낼 수 있는 경우
        studytime = int(arr[i + 1][1][:2]) * 60 + int(arr[i + 1][1][3:]) - (
                    int(arr[i][1][:2]) * 60 + int(arr[i][1][3:]))
        if studytime >= int(arr[i][2]):
            answer.append(arr[i][0])
            # 중단한 과제가 남아있고, 다음 과제를 하기전에 중단한 과제를 할 수 있는 경우
            if hmwrk:
                sprtime = studytime - int(arr[i][2])
                while sprtime > 0:
                    # 중단한 과제를 다음과제 전에 마무리 할 수 있는 경우
                    if hmwrk[-1][1] <= sprtime:
                        answer.append(hmwrk[-1][0])
                        sprtime -= hmwrk[-1][1]
                        hmwrk.pop()
                        if len(hmwrk) == 0:
                            break
                    # 과제를 마무리하지 못하고 조금만 하는 경우
                    else:
                        hmwrk[-1][1] -= sprtime
                        sprtime = 0
        # 다음 과제를 해야해서 과제를 중단해야 하는 경우
        else:  # studytime < int(arr[i][2])
            runtime = int(arr[i][2]) - studytime
            hmwrk.append([arr[i][0], runtime])
    # 제일 마지막에 시작한 과제를 추가한다.
    answer.append(arr[-1][0])
    # 중단한 과제가 남아있다면 역순으로 추가한다.
    if hmwrk:
        while hmwrk:
            answer.append(hmwrk[-1][0])
            hmwrk.pop()

    return answer
