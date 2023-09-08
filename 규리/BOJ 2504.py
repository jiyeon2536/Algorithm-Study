txt = list(map(str, input()))
stack = []
result = -1
calc1 = []

# 올바른 괄호열인지 확인
for t in txt:
    if t in '([':
        stack.append(t)
    else:
        if t == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                result = 0
                break
        elif t == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                result = 0
                break

    if result == 0:
        break

if len(stack) > 0:
    result = 0

# 올바른 괄호열이 아니라면
if result == 0:
    print(0)
# 올바른 괄호열이라면
else:
    # () -> 2, [] -> 3
    # (2[3])(3)
    for i in range(len(txt)):
        if txt[i] == '(':
            if txt[i+1] == ')':
                calc1.append('2')
            else:
                calc1.append('(')
        elif txt[i] == ')':
            if txt[i-1] != '(':
                calc1.append(')')
        elif txt[i] == '[':
            if txt[i+1] == ']':
                calc1.append('3')
            else:
                calc1.append('[')
        elif txt[i] == ']':
            if txt[i-1] != '[':
                calc1.append(']')

    # 중위표기법
    # (2*(2+3*(3))+2*(3))
    calc2 = []
    for i in range(len(calc1)):
        if calc1[i] == '(':
            if i == 0:
                calc2.append('2')
                calc2.append('*')
                calc2.append('(')
            else:
                if calc1[i-1].isdigit() or calc1[i-1] in ')]':
                    calc2.append('+')
                    calc2.append('2')
                    calc2.append('*')
                    calc2.append('(')
                else:
                    calc2.append('2')
                    calc2.append('*')
                    calc2.append('(')
        elif calc1[i] == '[':
            if i == 0:
                calc2.append('3')
                calc2.append('*')
                calc2.append('(')
            else:
                if calc1[i - 1].isdigit() or calc1[i - 1] in ')]':
                    calc2.append('+')
                    calc2.append('3')
                    calc2.append('*')
                    calc2.append('(')
                else:
                    calc2.append('3')
                    calc2.append('*')
                    calc2.append('(')
        elif calc1[i] == ')' or calc1[i] == ']':
            calc2.append(')')
        else:
            if calc1[i-1] in '])' or calc1[i-1].isdigit():
                calc2.append('+')
            calc2.append(str(calc1[i]))
    calc = '('
    for x in calc2:
        calc += x
    calc += ')'

    # 후위표기법
    # 2233*+*23*+
    stack = [0]*100
    icp = {'(': 3, '*': 2, '+': 1}
    isp = {'(': 0, '*': 2, '+': 1}
    top = -1
    susik = ''
    for x in calc:
        if x not in '(+*)':
            susik += x
        elif x == ')':
            while stack[top] != '(':
                susik += stack[top]
                top -= 1
            top -= 1
        else:
            if top == -1 or isp[stack[top]] < icp[x]:
                top += 1
                stack[top] = x
            elif isp[stack[top]] >= icp[x]:
                while top > -1 and isp[stack[top]] >= icp[x]:
                    susik += stack[top]
                    top -= 1
                top += 1
                stack[top] = x

    # 계산
    # 28
    stack = [0]*100
    top = -1
    for x in susik:
        if x not in '+*':
            top += 1
            stack[top] = int(x)
        else:
            op1 = stack[top]
            top -= 1
            op2 = stack[top]
            top -= 1
            if x == '+':
                top += 1
                stack[top] = op1 + op2
            elif x == '*':
                top += 1
                stack[top] = op1 * op2
    print(stack[top])
