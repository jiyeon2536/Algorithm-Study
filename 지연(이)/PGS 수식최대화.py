from itertools import permutations
def calcul(num1, num2, o):
    if o=='*':
        return num1*num2
    elif o=='+':
        return num1+num2
    return num1-num2

def function1(num,oper,o):
    new_num = []
    new_oper = []
    for i in range(len(oper)):
        if oper[i]==o:
            num[i+1]=calcul(num[i],num[i+1],oper[i])
        else:
            new_num.append(num[i])
            new_oper.append(oper[i])
    new_num.append(num[-1])
    return new_num, new_oper

def solution(expression):
    answer = 0
    oper = set()
    nums, opers = [],[]
    tmp = ''
    for i in range(len(expression)):
        if expression[i].isdigit():
            tmp+=expression[i]
        else:
            oper.add(expression[i])
            nums.append(int(tmp))
            opers.append(expression[i])
            tmp=''
    nums.append(int(tmp))
    
    priorities = permutations(list(oper),len(oper))
    for priority in priorities:
        num, oper = nums[:], opers[:]
        for o in priority:
            num,oper = function1(num, oper, o)
        answer = max(answer, abs(num[0]))
    return answer
print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
