def solution(storey):
    answer = 0
    count = 0
    while storey:
        # 2자리 확인해봤을 때 55 이상이면 5에 대한 처리가 필요함 => 5 이상일 때 올림
        if storey % (10 ** (count + 2)) // (10 ** count) >= 55:
            now = storey % (10 ** (count + 2)) // (10 ** count)
            now = now % 10
            if now >= 5:
                storey += (10 - now) * (10 ** count)
                answer += 10 - now
            else:
                answer += now
                storey -= now * (10 ** count)
                print('here')
        # 55 이상이 아닌 경우 6 이상일 때 올림, 나머지는 내림
        else:
            if storey % (10 ** (count + 1)):
                now = storey % (10 ** (count + 1)) // (10 ** count)
            else:
                now  = 0
            if now >= 6:
                answer += 10 - now
                storey += (10 - now) * (10 ** count)
            else:
                answer += now
                storey -= now * (10 ** count)
        count += 1
        
    return answer
