def solution(plans):
    answer = []
    for i in range(len(plans)):
        plans[i][1], plans[i][2] = int(plans[i][1][:2])*60+int(plans[i][1][3:]), int(plans[i][2])
    plans.sort(key=lambda x:x[1])
    # print(plans)

    now_time = plans[0][1]
    stack = []
    for i in range(len(plans)-1):
        # print()
        # print(now_time, plans[i][0], plans[i+1][1])
        if now_time+plans[i][2] > plans[i+1][1]:
            stack.append( (plans[i][0], plans[i][2]-(plans[i+1][1]-now_time) ))
            now_time = plans[i+1][1]
            # print('now time > nxt start time')
            # print(stack, now_time)
        else:
            # print('now time <= nxt start time')
            answer.append(plans[i][0])
            now_time += plans[i][2]
            # print('while')
            while stack:
                name, playtime = stack.pop()
                # print(f'name:{name}, playtime:{playtime}, nowtime:{now_time}')
                if now_time+playtime>plans[i+1][1]:
                    stack.append((name, playtime - (plans[i+1][1]-now_time) ))
                    now_time = plans[i+1][1]
                    # print('break ', stack)
                    break
                else:
                    answer.append(name)
                    now_time = now_time+playtime

            # 현시간 기준, 작업하던거 모두 작업했는데도 시간 남으면, 다음 nxt시작 시간으로 가야함
            if not stack:
                now_time = plans[i+1][1]
            # print('while end')
            # print(f'now time : {now_time}')

    answer.append(plans[-1][0])
    while stack:
        answer.append(stack.pop()[0])

    return answer



# print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
# korean english math
# print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
# science history computer music
# print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))
# bbb ccc aaa
# print(solution([["science", "12:40", "80"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
# science history computer music
# print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "20"], ["ccc", "12:20", "20"],["ddd","12:30","20"],["eee","12:50","20"],["fff","13:30","100"],["ggg","14:00","100"],["hhh","14:30","100"],["ttt","15:00","100"]]))
# d e c b t h g f a
# print(solution( [["a", "09:00", "10"], ["b", "09:10", "10"], ["c", "09:15", "10"], ["d", "09:30", "10"], ["e", "09:35", "10"]]))
# a c b e d
# print(solution( [["a", "09:00", "30"], ["b", "09:20", "10"], ["c", "09:40", "10"]]))
# b a c
# print(solution([["A", "11:50", "30"], ["B", "13:00", "20"], ["C", "13:10", "30"]]))
#  A C B
