import math

def solution(r1, r2):
    answer = 0
    for x in range(1,r2+1):
        mx = math.floor((r2**2 - x**2)**0.5)
        if x>r1:
            mn = 0
        else:
            mn = math.ceil((r1**2 - x**2)**0.5)
        answer += (mx-mn+1)
        # print((x,mx,mn,(mx-mn+1)))
    answer *= 4
    return answer
