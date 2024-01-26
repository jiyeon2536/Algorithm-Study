def solution(n, s):
    if n>s:
        return [-1]
    answer = [s//n]*n
    if s-(s//n)*n:
        i = n-1
        val = s-(s//n)*n
        while i>-1 and val:
            answer[i]+=1
            val-=1
            i-=1
    return answer
