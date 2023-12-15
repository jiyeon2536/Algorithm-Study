def solution(plans):
    from collections import deque
    answer = []
    # 시간순으로 정렬
    plans.sort(key=lambda x:x[1])
    print(plans)
    n = len(plans) # 계획의 수
    now = plans[0][1] # 현재 시간
    stack = deque() # 미뤄둔 일
    for idx in range(n-1):
        cur = plans[idx]
        nxt = plans[idx+1]
        
        # 분으로 계산
        times = int(cur[1][:2]) * 60 + int(cur[1][3:]) + int(cur[2])
        d_hour = times // 60
        d_min = times % 60
        
        # 한 자릿수인 경우 보정
        if d_hour < 10:
            d_hour = '0' + str(d_hour)
        if d_min < 10:
            d_min = '0' + str(d_min)
            
        d_time = f'{d_hour}:{d_min}'
        
        # 완료 시간이 다음 일정보다 빨리 마칠 때
        if d_time < nxt[1]:
            answer.append(cur[0])
            # 미뤄둔 일이 있는지 체크
            if stack:
                # 다음 시작 시간까지 일 처리
                later_able = (int(nxt[1][:2]) * 60 + int(nxt[1][3:])) - times
                while stack:
                    later, later_time = stack.pop()
                    # 일할 수 있는 시간 체크
                    # 남는 시간이 남은 시간보다 크다면 가능
                    if later_able >= later_time:
                        later_able -= later_time
                        answer.append(later)
                    # 남는 시간이 부족하면 남는 시간만큼 빼주고 다시 넣기
                    else:
                        later_time -= later_able
                        stack.append((later, later_time))
                        break
                    if later_able == 0:
                        break                    
        # 완료 시간이 다음 일정 시작 시간과 동일할 때
        elif d_time == nxt[1]:
            answer.append(cur[0])
            
        # 다음 일정 시작 전에 마치지 못하는 경우
        else:
            # 사용할 수 있는 시간 구하기
            able = (int(nxt[1][:2]) * 60 + int(nxt[1][3:])) - (int(now[:2]) * 60 + int(now[3:]))
            # 미뤄둔 일에 이름과 남은 시간 추가
            stack.append((cur[0], int(cur[2]) - able))
            
        now = nxt[1] # 현재 시간 갱신
    
    # 마지막 친구는 넣기
    answer.append(plans[-1][0])
    # 미뤄둔 일에 남은 친구 하나씩 넣어주기
    while stack:
        last, last_time = stack.pop()
        answer.append(last)
    return answer
