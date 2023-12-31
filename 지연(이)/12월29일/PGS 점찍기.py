
def solution(k, d):
    answer = 0
    for a in range(1000001):
        if d<a*k:
            break
        answer+= int(( d**2 - (a*k)**2)**0.5)//k + 1
    return answer
