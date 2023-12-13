bracket = input()
stack = []
is_correct = True

for i in bracket:
    # 여는 괄호라면 일단 추가
    if i in ['(', '[']:
        stack.append(i)
        continue

    # 스택에 요소가 없을 경우
    if len(stack) == 0:
        # 여는 괄호라면 추가
        if i in ['(', '[']:
            stack.append(i)
            continue
        # 여는 괄호가 아니면 올바른 형식이 아님
        else:
            is_correct = False
            break

    # 소괄호 검사
    if i == ')':
        # 스택 마지막 요소가 숫자 또는 여는 소괄호가 아닐 경우
        if stack[-1] in ['[', ']', ')']:
            is_correct = False
            break
        # 여는 소괄호라면 pop 후 정수 값을 추가
        elif stack[-1] == '(':
            stack.pop()
            stack.append(2)
        # 정수라면
        else:
            tmp = 0

            # 여는 괄호가 나올 때까지 정수를 더하다가
            # 여는 괄호를 만나면 곱 연산 후 스택에 추가
            while True:
                if len(stack) == 0:
                    is_correct = False
                    break

                next = stack[-1]

                if next in ['[', ']', ')']:
                    is_correct = False
                    break
                elif next == '(':
                    stack.pop()
                    stack.append(tmp * 2)
                    break
                else:
                    stack.pop()
                    tmp += next

    # 중괄호 검사
    # 로직은 소괄호와 같음
    if i == ']':
        if stack[-1] in ['(', ')', ']']:
            is_correct = False
            break
        elif stack[-1] == '[':
            stack.pop()
            stack.append(3)
        else:
            tmp = 0

            while True:
                if len(stack) == 0:
                    is_correct = False
                    break

                next = stack[-1]

                if next in ['(', ')', ']']:
                    is_correct = False
                    break
                elif next == '[':
                    stack.pop()
                    stack.append(tmp * 3)
                    break
                else:
                    stack.pop()
                    tmp += next

res = 0

# 스택에 남은 정수 혹은 괄호 검사
while stack:
    tmp = stack.pop()

    # 남은 괄호가 있다면 올바른 형식이 아님
    if tmp in ['(', ')', '[', ']']:
        is_correct = False
        break
    else:
        res += tmp

if is_correct:
    print(res)
else:
    print(0)
