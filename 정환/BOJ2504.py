import sys
input = sys.stdin.readline

arr = list(input().strip())


stack = []
stack.append(arr[0])
num_stack = []
is_ans = True

spc = '()[]'

i = 1
if len(arr) == 1:
    is_ans = False

# 미친 while 문 start
while len(arr) > 1:
    # 더 이상 연산 할 요소가 없음
    if i == len(arr):
        is_ans = False
        break
    # 스택에 최근 요소 중 여는 괄호의 종류가 현재 닫는 괄호의 종류와 다를 때
    if stack[-1] == '(' and arr[i] == ']':
        is_ans = False
        break
    elif stack[-1] == '[' and arr[i] == ')':
        is_ans = False
        break
    # 같을 때
    elif stack[-1] == '(' and arr[i] == ')':
        # 직전 인덱스 요소가 닫는괄호라면
        if arr[i - 1] == '(':
            # 직전 인덱스 요소를 2로 변경하고 스택, while 문 초기화하여 재순회
            arr[i - 1] = 2
            arr.pop(i)
            stack.clear()
            stack.append(arr[0])
            i = 1
        # 직전 인덱스 요소가 숫자라면
        elif str(arr[i - 1]) not in spc:
            # 상응하는 연산 진행 후 위처럼 초기화 하여 재순회
            arr[i - 1] *= 2
            arr.pop(i)
            stack.clear()
            stack.append(arr[0])
            i = 1
        # 둘 다 아닐 경우라면 두 괄호의 종류가 다르거나
        # 반대방향을 보는 괄호를 만나 틀린 형식일 경우
        else:
            is_ans = False
            break
    # 위와 같고 괄호의 종류만 대괄호일 경우
    elif stack[-1] == '[' and arr[i] == ']':
        if arr[i - 1] == '[':
            arr[i - 1] = 3
            arr.pop(i)
            stack.clear()
            stack.append(arr[0])
            i = 1
        elif str(arr[i - 1]) not in spc:
            arr[i - 1] *= 3
            stack.clear()
            stack.append(arr[0])
            arr.pop(i)
            i = 1
        else:
            is_ans = False
            break
    # 현재 인덱스 요소와 직전 인덱스 요소가 숫자일 경우에는
    # 두 숫자를 더하는 연산 진행한 후에 초기화 후 재순회
    elif str(arr[i]) not in spc and str(arr[i - 1]) not in spc:
        arr[i - 1] += arr[i]
        arr.pop(i)
        stack.clear()
        stack.append(arr[0])
        i = 1
    else:
        if str(arr[i]) not in spc:
            # ( 3 ) 와 같이 숫자가 괄호로 쌓인 경우를 체크하여 알맞은 연산 후 재순회
            if 0< i < len(arr) - 1 and arr[i - 1] == '(' and arr[i + 1] == ')':
                arr[i - 1] = arr[i] * 2
                arr.pop(i)
                arr.pop(i)
                stack.clear()
                stack.append(arr[0])
                i = 1
            elif 0< i < len(arr) - 1 and arr[i - 1] == '[' and arr[i + 1] == ']':
                arr[i - 1] = arr[i] * 3
                arr.pop(i)
                arr.pop(i)
                stack.clear()
                stack.append(arr[0])
                i = 1
            else:
                i += 1
            # 왜 이렇게 걸어놨는지 잊어버렸지만 고장날까봐 그대로 두었음
            continue
        # 계속 여는 괄호를 만나는 경우
        else:
            stack.append(arr[i])
            i += 1
# 올바른 수식이 맞으면 arr 에 남아있는 1개의 숫자 출력,
# 올바른 수식이 아닐경우에는 0 을 출력
if is_ans == True:
    print(* arr)
else:
    print(0)
