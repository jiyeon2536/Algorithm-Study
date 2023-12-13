def solution(expression):
    from itertools import permutations
    answer = 0
    oper = ['*','+','-']
    def add(a, b):
        return a + b
    def sub(a, b):
        return b - a
    def mul(a, b):
        return a * b
    cal = {
        '*' : mul,
        '+' : add,
        '-' : sub
    }
    perms = permutations(oper,3)
    for perm in perms:
        pri = {perm[0] : 3, perm[1] : 2, perm[2] : 1 }
        # 중위식을 후위연산식으로
        postfix = []
        # 숫자를 받을 문자열 변수
        num = ''
        # oper 받을 리스트
        opr = []
        for ch in expression:
            if ch.isdigit():
                num += ch
            else:
                postfix.append(int(num))
                num = ''
                # opr이 비어있지 않거나, ch의 우선순위가 opr의 top 기호의 우선순위보다 낮거나 같을수록
                while opr and pri[ch] <= pri[opr[-1]]:
                    postfix.append(opr.pop())
                # 위에 해당되지 않는다면 opr에 추가
                opr.append(ch)
        if num:
            postfix.append(int(num))
        # opr에 남아 있는 기호 다 pop
        while opr:
            postfix.append(opr.pop())
            
        # 후위연산
        res = []

        for char in postfix:
            # 숫자라면 res에 append
            if isinstance(char, int):
                res.append(char)
            # 기호라면 연산 후 append
            else:
                a = res.pop()
                b = res.pop()
                cal_val = cal[char](a, b)
                res.append(cal_val)

        if answer < abs(res[0]):
            answer = abs(res[0])
    return answer
