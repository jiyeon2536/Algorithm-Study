def solution(plans):
    answer = []
    for i in plans:
        i[1] = (int(i[1][:2]) * 60 + int(i[1][3:5]))
        i[2] = int(i[2])
        print(i[2])
    stack = []
    
    
    plans.sort(key=lambda x: x[1])
    now_time = plans[0][1]
    # print(f'현재 시각 : {now_time}')
    
    
    for j in range(1, len(plans)):
#         # 이전 과제 완료 예상 시간
        previous = now_time + plans[j - 1][2]
        # print(previous)
#         # 현재 작업이 시작 시간의 시각이 이전 작업 종료 시간의 시각과 같거나 작을 경우
        
        if plans[j][1] < previous:
            now_time = plans[j][1]
            stack.append([plans[j - 1][0], previous - now_time])
        elif plans[j][1] > previous:
            answer.append(plans[j - 1][0])
            while previous <= plans[j][1]:
                if stack:
                    if previous + stack[-1][1] <= plans[j][1]:
                        now_time = previous + stack[-1][1]
                        previous = now_time
                        answer.append(stack.pop()[0])
                    else:
                        now_time = plans[j][1]
                        stack[-1][1] -= now_time - previous
                        break
                else:
                    now_time = plans[j][1]
                    break
            if not stack:
                now_time = plans[j][1]
        else:
            answer.append(plans[j - 1][0])
            now_time = plans[j][1]
                    
        if j == len(plans) - 1:
            answer.append(plans[j][0])
    while stack:
        answer.append(stack.pop()[0])

    
    return answer
