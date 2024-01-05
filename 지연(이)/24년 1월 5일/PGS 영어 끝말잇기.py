import math
def solution(n, words):
    answer = [0,0]
    check = set()
    for i in range(len(words)):
        if words[i] in check or (i>0 and words[i-1][-1] != words[i][0]):
            answer[0] = i%n+1
            answer[1] = math.ceil((i+1)/n)
            break
        check.add(words[i])
    return answer
