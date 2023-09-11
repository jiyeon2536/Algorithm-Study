from collections import deque
import sys
input = sys.stdin.readline

# 괄호 입력
arr = list(input().strip())

# 스택 생성
stack = deque()

# 괄호 성립 조건 만족 여부
condition = True

# 괄호를 순회
for oper in arr:
    # 닫는 기호가 아니라면 스택에 push
    if oper not in [')',']']:
        stack.append(oper)
    # 닫는 기호가 들어온다면
    else:
        try:
            # 소괄호인 경우
            if oper == ')':
                # 가장 마지막에 pop되는 값을 받을 top 변수 생성
                # ( 기호를 만날때까자 pop되는 숫자 리스트
                top = 0
                nums = deque()
                # 여는 기호를 만날떄까지 순회
                while top != '(':
                    # 입력값들 중 우선순위가 존재하지 않고, 적합한 괄호쌍이 존재했다면,  이미 계산되어 숫자여야함
                    # top이 여는 괄호라면 pop
                    if stack[-1] == '(':
                        top = stack.pop()
                        if nums: # nums가 존재한다면 nums 내의 값 모두 더하여 * 2
                            stack.append(sum(nums) * 2)
                        else: # 존재하지 않는다면 2 입력
                            stack.append(2)
                            
                    # top이 숫자라면 여는 괄호 만들 때까지
                    elif str(stack[-1]).isdigit():
                        top = stack.pop()
                        nums.append(top)
                    else: 
                    # 대괄호나, ) 기호일시 조건 미충족 체크 후 break
                        condition = False
                        break
                # 조건 불만족하면 전체 fot문도 break
                if condition == False:
                    break
                    
            # 대괄호
            elif oper == ']':
                top = 0
                nums = deque()
                while top != '[':
                    # top이 여는 괄호라면
                    if stack[-1] == '[':
                        top = stack.pop()
                        if nums: # nums가 1개일때 2개일떼 0개일때
                            stack.append(sum(nums) *3)
                        else:
                            stack.append(3)
                    # top이 숫자라면 여는 괄호 만들 때까지
                    elif str(stack[-1]).isdigit():
                        top = stack.pop()
                        nums.append(top)
                    else:
                        condition = False
                        break
                if condition == False:
                    break
        # 여는 괄호가 닫는 괄호보다 부족한 경우 error발생
        # 조건 미충족 체크 후 break
        except:
            condition = False
            break

# 여는 괄호가 닫는 괄호보다 많은 경우
# 최종 결과를 위해 sum하는 과정에서 error 발생 -> 예외처리하여 0 출력
# 이전에 오류 발생하였거나, 적절한 괄호쌍이 아이었을 경우 -> 0 출력
# 조건 모두 만족한 경우 sun한 결과 출력# 입력값들 중 우선순위가 존재하지 않고, 적합한 괄호쌍이 존재했다면,  이미 계산되어 숫자여야함'
try:
    if condition:
        print(sum(stack))
    else:
        print(0)

except:
    print(0)
