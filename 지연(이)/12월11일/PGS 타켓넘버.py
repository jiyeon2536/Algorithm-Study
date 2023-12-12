# 라이브러리 vs 비트연산자? while dfs

def solution(numbers, target):
    answer = 0
    stack = ['']
    combinations = []
    while stack:
        s = stack.pop()
        if len(s)==len(numbers):
            combinations.append(s)
            continue
        stack.append(s+'0')
        stack.append(s+'1')


    for combination in combinations:
        tmp = 0
        for i in range(len(numbers)):
            if combination[i]=='1':
                tmp+=numbers[i]
            else:
                tmp-=numbers[i]
        if tmp==target:
            answer+=1

    return answer
