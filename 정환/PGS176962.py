def solution(plans):
    answer = []
    for i in plans:
        i[1] = [int(i[1][:2]), int(i[1][3:5])]
        i[2] = int(i[2])
        # print(i[1])
    stack = []
    
    
    plans.sort(key=lambda x: (x[1][0], x[1][1], x[2]))
    now_time = plans[0][1]
    # print(f'현재 시각 : {now_time}')
    for j in range(1, len(plans)):
        
        previous = now_time[:]
        
        if previous[1] + plans[j - 1][2] >= 60:
            
            previous = [previous[0] + (previous[1] + plans[j - 1][2]) // 60, (previous[1] + plans[j - 1][2]) % 60]
            # print(plans[j - 1], "**")
            # print((previous[1] + plans[j - 1][2]) % 60, "**")
            # print(previous, "**")
        else:
            previous[1] += plans[j - 1][2]
        
        # 현재 작업이 시작 시간의 시각이 이전 작업 종료 시간의 시각과 같거나 작을 경우
        if plans[j][1][0] <= previous[0]:
            now_time = [plans[j][1][0], plans[j][1][1]]
            # 종료시간보다 현재 작업시간이 빠를 경우
            if (plans[j][1][0] == previous[0] and plans[j][1][1] <= previous[1]) or (plans[j][1][0] < previous[0]):
                if now_time[0] == previous[0]:
                    if previous[1] - now_time[1] > 0:

                        stack.append([plans[j - 1][0], previous[1] - now_time[1]])
                    else:
                        # print("hi", j)
                        answer.append(plans[j - 1][0])
                else:
                    if previous[1] + (previous[0] - now_time[0]) * 60 - now_time[1] > 0:

                        stack.append([plans[j - 1][0], previous[1] + (previous[0] - now_time[0]) * 60 - now_time[1]])
                    else:
                        if stack:
                            while stack:
                                tmp = stack.pop()
                                if now_time[0] > previous[1]:
                                    if now_time[1] - tmp[1] < 0:
                                        tmp2 = (now_time[0] - previous[1]) * 60 - tmp[1]
                                        if tmp2 <= 0:
                                            answer.append(tmp[0])
                                        else:
                                            stack.append([tmp[0], tmp2])
                                else:
                                    if (now_time[0] - previous[1]) - tmp[1] <= 0:
                                        answer.append([tmp[0]])
                                    else:
                                        stack.append([tmp[0], (now_time[0] - previous[1]) - tmp[1]])
                                        
                        answer.append(plans[j - 1][0])
            # elif plans[j][1][0] == previous[0] and plans[j][1][1] >= previous[1]:
            #     if plans[j][1][1] == previous[1]:
            #         answer.append(plans[j - 1][0])
            #     else:
            #         # plans[j][1][1] >previous[1]
            #         if stack:
            #             while stack:
            #                 if plans[j][1][1] - previous[1] < stack[-1][1]:
            #                     stack[-1][1] -= plans[j][1][1] - previous[1]
            #                     break
            #                 elif plans[j][1][1] - previous[1] == stack[-1][1]:
            #                     answer.append(stack.pop()[0])
            #                     break
            #                 else:
            #                     answer.append(stack.pop()[0])
                
        elif (plans[j][1][0] > previous[0]) or(plans[j][1][0] == previous[0] and plans[j][1][1] >= previous[1]):
            now_time = [plans[j][1][0], plans[j][1][1]]
            if now_time[0] == previous[0]:
                if stack:
                    while stack:
                        if (now_time[1] - previous[1]) < stack[-1][1]:
                            stack[-1][1] -= now_time[1] - previous[1]
                            break
                        elif (now_time[1] - previous[1]) == stack[-1][1]:
                            answer.append(stack.pop()[0])
                            break
                        else:
                            answer.append(stack.pop()[0])
            else:
                if stack:
                    while stack:
                        if (((now_time[0] - previous[0]) * 60 + now_time[1]) - previous[1] < stack[-1][1]):
                            stack[-1][1] -= ((now_time[0] - previous[0]) * 60 + now_time[1]) - previous[1]
                            break
                        elif (((now_time[0] - previous[0]) * 60 + now_time[1]) - previous[1] == stack[-1][1]):
                            answer.append(stack.pop()[0])
                            break
                        else:
                            answer.append(stack.pop()[0])
                        
                
            answer.append(plans[j - 1][0])
        if j == len(plans) - 1:
            answer.append(plans[-1][0])
        
            
        # print(f'스택 : {stack}')
    if stack:
        while stack:
                answer.append(stack.pop()[0])
    # print(plans)
    
    return answer
