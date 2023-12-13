# 요격 시스템

def solution(targets):
    answer = 1
    n = len(targets)
    targets = sorted(targets, key = lambda x : x[1])
    end = targets[0][1]
    for i in range(1, n):
        if targets[i][0] >= end:
            end = targets[i][1]
            answer += 1
    return answer