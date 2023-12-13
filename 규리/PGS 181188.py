def solution(targets):
    answer = 1
    targets.sort(key=lambda x:(x[1], x[0]))
    
    E = targets[0][1]
    N = len(targets)

    for i in range(1, N):
        start, end = targets[i]
        if E <= start:
            answer += 1
            E = end
    
    return answer
