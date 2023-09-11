import sys
input = sys.stdin.readline

N = int(input().strip())

# 양수
positive = []
#음수
negative = []
# 0이 있을경우, 0도 담는다. 음수가 홀수일 경우에 0과 곱함
zero = []

# 리스트를 돌면서 양수는 양수리스트, 음수는 음수리스트, 0은 zero 리스트에 담는다.
for _ in range(N):
    num = int(input().strip())
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
    else:
        zero.append(num)

# 높은값끼리 곱해야 최대값이 나오므로 정렬
positive.sort()
# 음수도 두 수씩 묶으면 양수이고, 높은 숫자끼리 묶여야 최대값
negative.sort()

posi_sum = 0
nega_sum = 0

# 양수에 담긴 수들이 짝수개일때
if len(positive) % 2 == 0:
    # 두 수씩 묶어 곱하여 posi_sum에 더하는데
    for i in range(0, len(positive), 2):
        # 이 때, 해당 숫자가 1일 경우에는 두 수를 곱하는 것 보다 각각 더하는 것이 더 높음
        if positive[i] == 1:
            posi_sum += positive[i + 1] + 1
        else:
            posi_sum += (positive[i] * positive[i + 1])
# 홀수일 경우에는 가장 앞자리 숫자를 빼서 먼저 더한 후, 위와같이 진행 (짝수개 or 0 개가 됨)
else:
    posi_sum += positive.pop(0)
    if len(positive) >= 2:
        for j in range(0, len(positive), 2):
            if positive[j] == 1:
                posi_sum += positive[j + 1] + 1
            else:
                posi_sum += (positive[j] * positive[j + 1])

# 음수도 비슷하게 진행하지만, 음수인 경우에는 [-1 , -1] 인 경우에
# 두 수를 곱하여 더하면 양수가 되지만, 각각 더하면 음수값을 더하게 되므로
# -1 인 경우도 함께 묶어서 진행
if len(negative) % 2 == 0:
    for x in range(0, len(negative), 2):
        nega_sum += (negative[x] * negative[x + 1])
# 음수의 개수가 홀수인 경우에 절대값이 가장 낮은 음수인 마지막 요소를 빼서 먼저 더한다.
else:
    nega_sum += negative.pop()
    # 만약 zero 에 숫자 0 이 들어있다면, 짝수를 만들기 위해 먼저 뺀 음수 요소를 곱하여 0으로 만든다.
    if zero and nega_sum != 0:
        nega_sum = 0
    if len(negative) >= 2:
        for y in range(0, len(negative), 2):
            nega_sum += (negative[y] * negative[y + 1])

print(posi_sum + nega_sum)