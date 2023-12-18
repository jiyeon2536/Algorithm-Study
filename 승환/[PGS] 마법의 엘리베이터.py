def solution(storey):
    answer = 0
    # 재귀로 풀 수 있다.
    temp = list(str(storey))
    chk = 0
    for i in range(len(temp) - 1, -1, -1):
        if int(temp[i]) > 5:
            answer += (10 - int(temp[i]))
            if i - 1 >= 0:
                temp[i - 1] = int(temp[i - 1]) + 1
            if i == 0:
                answer += 1
        # 일의 자리가 5인 경우
        elif int(temp[i]) == 5:
            # 십의 자리가 존재하고
            if i - 1 >= 0:
                # 십의 자리가 5이상일 경우
                if int(temp[i - 1]) >= 5:
                    answer += (10 - int(temp[i]))
                    if i - 1 >= 0:
                        temp[i - 1] = int(temp[i - 1]) + 1
                # 십의 자리가 5미만일 경우
                else:
                    answer += int(temp[i])
            else:
                answer += int(temp[i])    
        else:
            answer += int(temp[i])
    return answer
