answer = []
str1 = ''
str2 = ''

def dfs(now, lst, tickets, visit):
    global answer 
    if len(lst)==len(tickets)+1:
        str1 = ''.join(lst)
        str2 = ''.join(answer)
        if not answer or str1<str2:
            answer = lst[:]
        return 
    for i in range(len(tickets)):
        start, end = tickets[i][0], tickets[i][1]
        if now == start and not visit[i]:
            visit[i]=1
            lst.append(end)
            dfs(end, lst, tickets, visit)
            lst.pop()
            visit[i]=0


def solution(tickets):
    global answer
    
    now = "ICN"
    visit = [0]*len(tickets)
    dfs(now, ["ICN"], tickets, visit)
    return answer
