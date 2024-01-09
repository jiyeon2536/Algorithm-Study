def solution(users, emoticons):
    answer = [0, 0]

    def calculate(llst):
        numAndPrice = [0,0]
        for userInfo in users:
            Price = 0
            for k in range(len(llst)):
                if llst[k]>=userInfo[0]:
                    Price+=emoticons[k]*((100-llst[k])/100)
            if Price>=userInfo[1]:
                Price = 0
                numAndPrice[0]+=1
            numAndPrice[1]+=Price
        numAndPrice[1]=int(numAndPrice[1])
        return numAndPrice

    def recursive(lst):
        if len(lst)==len(emoticons):
            numAndPrice = calculate(lst)
            if numAndPrice[0]>answer[0]:
                answer[0] = numAndPrice[0]
                answer[1] = numAndPrice[1]
            elif  numAndPrice[0]==answer[0] and numAndPrice[1]>answer[1]:
                answer[1] = numAndPrice[1]
            return
        for j in range(40,0,-10):
            lst.append(j)
            recursive(lst)
            lst.pop()
    for i in range(40,0,-10):
        recursive([i])
    return answer

print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
