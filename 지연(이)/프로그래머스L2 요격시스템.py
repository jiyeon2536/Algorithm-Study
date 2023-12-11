def solution(targets):
    answer = 0
    targets.sort(key=lambda x : x[0])

    e1 = targets[0][1]
    for i in range(len(targets)):
        if e1<=targets[i][0]:
            answer += 1
            e1 = targets[i][1]
        elif targets[i][0]<e1<=targets[i][1]:
            pass
        else:
            e1 = targets[i][1]
        if i==len(targets)-1:
            answer+=1
    return answer
