def solution(expression):
    answer = 0  # mx 값
    number = ''
    # * > + > -
    pri = {
        '*':3, '+':2, '-':1
    }
    num = []
    opr = []
    for i in expression:
        temp = i
        try:
            n = int(i)
            number += temp
        except:
            num.append(number)
            number = ''
            while opr and pri[i] <= pri[opr[-1]]:
                num.append(opr.pop())
            opr.append(i)
    num.append(number)
    while len(opr) > 0:
        num.append(opr.pop())   
    res = []
    print(num)
    for i in range(len(num)):
        if num[i] in pri:
            if num[i] == '*':
                a1 = res.pop()
                a2 = res.pop()
                res.append(a1 * a2)
            elif num[i] == '+':
                a1 = res.pop()
                a2 = res.pop()
                res.append(a1 + a2)
            elif num[i] == '-':
                a1 = res.pop()
                a2 = res.pop()
                res.append(a2 - a1)
        else:
            res.append(int(num[i]))
    print(res)
    if abs(res[0]) > answer:
        answer = abs(res[0])

    # * > - > +
    number = ''
    pri = {
        '*':3, '+':1, '-':2
    }
    num = []
    opr = []
    for i in expression:
        temp = i
        try:
            n = int(i)
            number += temp
        except:
            num.append(number)
            number = ''
            while opr and pri[i] <= pri[opr[-1]]:
                num.append(opr.pop())
            opr.append(i)
    num.append(number)
    while len(opr) > 0:
        num.append(opr.pop())   
    res = []
    for i in range(len(num)):
        if num[i] in pri:
            if num[i] == '*':
                a1 = res.pop()
                a2 = res.pop()
                res.append(a1 * a2)
            elif num[i] == '+':
                a1 = res.pop()
                a2 = res.pop()
                res.append(a1 + a2)
            elif num[i] == '-':
                a1 = res.pop()
                a2 = res.pop()
                res.append(a2 - a1)
        else:
            res.append(int(num[i]))
    if abs(res[0]) > answer:
        answer = abs(res[0])

    # + > * > -
    number = ''
    pri = {
        '+':3, '-':1, '*':2
    }
    num = []
    opr = []
    for i in expression:
        temp = i
        try:
            n = int(i)
            number += temp
        except:
            num.append(number)
            number = ''
            while opr and pri[i] <= pri[opr[-1]]:
                num.append(opr.pop())
            opr.append(i)
    num.append(number)
    while len(opr) > 0:
        num.append(opr.pop())   
    res = []
    for i in range(len(num)):
        if num[i] in pri:
            if num[i] == '*':
                a1 = res.pop()
                a2 = res.pop()
                res.append(a1 * a2)
            elif num[i] == '+':
                a1 = res.pop()
                a2 = res.pop()
                res.append(a1 + a2)
            elif num[i] == '-':
                a1 = res.pop()
                a2 = res.pop()
                res.append(a2 - a1)
        else:
            res.append(int(num[i]))
    if abs(res[0]) > answer:
        answer = abs(res[0])

    # + > - > *
    number = ''
    pri = {
        '+':3, '*':1, '-':2
    }
    num = []
    opr = []
    for i in expression:
        temp = i
        try:
            n = int(i)
            number += temp
        except:
            num.append(number)
            number = ''
            while opr and pri[i] <= pri[opr[-1]]:
                num.append(opr.pop())
            opr.append(i)
    num.append(number)
    while len(opr) > 0:
        num.append(opr.pop())   
    res = []
    for i in range(len(num)):
        if num[i] in pri:
            if num[i] == '*':
                a1 = res.pop()
                a2 = res.pop()
                res.append(a1 * a2)
            elif num[i] == '+':
                a1 = res.pop()
                a2 = res.pop()
                res.append(a1 + a2)
            elif num[i] == '-':
                a1 = res.pop()
                a2 = res.pop()
                res.append(a2 - a1)
        else:
            res.append(int(num[i]))
    if abs(res[0]) > answer:
        answer = abs(res[0])

    # - > * > +
    number = ''
    pri = {
        '-':3, '+':1, '*':2
    }
    num = []
    opr = []
    for i in expression:
        temp = i
        try:
            n = int(i)
            number += temp
        except:
            num.append(number)
            number = ''
            while opr and pri[i] <= pri[opr[-1]]:
                num.append(opr.pop())
            opr.append(i)
    num.append(number)
    while len(opr) > 0:
        num.append(opr.pop())   
    res = []
    for i in range(len(num)):
        if num[i] in pri:
            if num[i] == '*':
                a1 = res.pop()
                a2 = res.pop()
                res.append(a1 * a2)
            elif num[i] == '+':
                a1 = res.pop()
                a2 = res.pop()
                res.append(a1 + a2)
            elif num[i] == '-':
                a1 = res.pop()
                a2 = res.pop()
                res.append(a2 - a1)
        else:
            res.append(int(num[i]))
    if abs(res[0]) > answer:
        answer = abs(res[0])

    # - > + > *
    number = ''
    pri = {
        '-':3, '*':1, '+':2
    }
    num = []
    opr = []
    for i in expression:
        temp = i
        try:
            n = int(i)
            number += temp
        except:
            num.append(number)
            number = ''
            while opr and pri[i] <= pri[opr[-1]]:
                num.append(opr.pop())
            opr.append(i)
    num.append(number)
    while len(opr) > 0:
        num.append(opr.pop())   
    res = []
    for i in range(len(num)):
        if num[i] in pri:
            if num[i] == '*':
                a1 = res.pop()
                a2 = res.pop()
                res.append(a1 * a2)
            elif num[i] == '+':
                a1 = res.pop()
                a2 = res.pop()
                res.append(a1 + a2)
            elif num[i] == '-':
                a1 = res.pop()
                a2 = res.pop()
                res.append(a2 - a1)
        else:
            res.append(int(num[i]))
    if abs(res[0]) > answer:
        answer = abs(res[0])


    return answer
