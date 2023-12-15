def solution(numbers, target):
    from collections import deque
    
    answer = 0
    
    # que 활용 : (합, 인덱스 겸 카운팅)
    que = deque()
    que.append((0,0))
    
    while que:
        sum_v, count = que.popleft()
        # 끝까지 갖다면 target과 동일한지 체크
        if count == len(numbers):
            if sum_v == target:
                answer += 1
        else:
            # count 자리의 값 더해주고 빼주기
            que.append((sum_v + numbers[count], count + 1))
            que.append((sum_v - numbers[count], count + 1))
    return answer
 
