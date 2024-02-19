import math

def solution(progresses, speeds):
    answer = []
    N = len(progresses)
    
    stack = []
    for i in range(N):
        stack.append(math.ceil((100-progresses[i])/speeds[i]))
    
    cnt = 1
    mx = stack[0]
    for i in range(1,N):
        if mx<stack[i]:
            answer.append(cnt)
            cnt=1
            mx = stack[i]
        else:
            cnt+=1
    answer.append(cnt)
    
    return answer
