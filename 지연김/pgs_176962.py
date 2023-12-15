# 과제 진행하기
def solution(plans):
    def calEndTime(start, playtime):
        hr = int(start[0:2])
        min = int(start[3:])
        playtime = int(playtime)
        tmp = min + playtime
        if tmp >= 120:
            hr += 2
            min = tmp - 120
        elif tmp >= 60:
            hr += 1
            min = tmp - 60
        else:
            min = tmp
        endtime = str(hr) + ':' + str(min)
        return endtime
        
    answer = []
    stack = []
    plans.sort(key=lambda x: x[1])
    n = len(plans)
    
    for i in range(n - 1):
        endtime = calEndTime(plans[i][1], plans[i][2])
        # 그 다음꺼가 먼저 시작되면 스택에 넣음
        if endtime > plans[i+1][1]:
            stack.append(plans[i][0])
        else:
            answer.append(plans[i][0])
    
    answer.append(plans[-1][0])
    
    while stack:
        answer.append(stack.pop())
    
    return answer