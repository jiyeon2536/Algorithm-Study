# 과제 진행하기
def solution(plans):
    answer = []
    stack = []
    new_plans = []

    for name, starttime, playtime in plans:
        start = int(starttime[0:2]) * 60 + int(starttime[3:])
        new_plans.append((name, start, int(playtime)))

    new_plans.sort(key=lambda x: x[1])
    n = len(new_plans)

    for i in range(n - 1):
        endtime = new_plans[i][1] + new_plans[i][2]
        
        # 그 다음꺼가 먼저 시작되면 스택에 넣음
        if endtime > new_plans[i + 1][1]:
            remain = endtime - new_plans[i + 1][1]
            stack.append([new_plans[i][0], remain])
            
        # 끝나는 시간이랑 다음꺼 시작시간에 사이비면 stack에꺼 그만큼 쭐여줌
        else:
            answer.append(new_plans[i][0])
            
            if endtime < new_plans[i + 1][1]:
                sparetime = new_plans[i + 1][1] - endtime
                while sparetime:
                    # 스택에 잇으면
                    if stack:
                        # 스택에 잇는 남은 시간을 빼줘야하는데
                        # 1. 스택에 잇는 남은 시간이 sparetime보다 긴 경우에는..
                        if stack[-1][1] > sparetime:
                            stack[-1][1] -= sparetime
                            break
                        # 2. 스택이 잇늠 남은 시간이 sparetime보다 짧은 경우에는
                        elif stack[-1][1] <= sparetime:
                            sparetime -= stack[-1][1]
                            answer.append(stack.pop()[0])
                    else:
                        break 


    answer.append(new_plans[-1][0])

    while stack:
        answer.append(stack.pop()[0])

    return answer