import sys
import math
input = sys.stdin.readline

n = int(input().strip())

# 소수 구하는 알고리즘
data = [True] * (n+1)
data[0] = False
data[1] = False

# 2에서 sqrt(n) + 1인 숫자에 대하여
# i가 나머지 없이 나누어진다면, False => 소수가 아님
for i in range(2, int(math.sqrt(n)) + 1):
    if data[i]:
        for j in range(i+i, n+1, i):
            data[j] = False

# 소수 리스트 : 소수 판단 결과 참인 경우만 추가
num_lst = []
for j in range(len(data)):
    if data[j]:
        num_lst.append(j)

# slow, fast, total, cnt
slow = fast = total = cnt = 0
while slow < len(num_lst):
    # total이 n보다 작다면
    # fast 값 더해주고 + 1
    if total < n:
        total += num_lst[fast]
        fast += 1

    # total이 n보다 크면
    # total 값 초기화, slow += 1, fast를 sloq에 맞춰줌
    elif total > n:
        total = 0
        slow += 1
        fast = slow

    # 소수의 합으로 n이 되었을 때
    # cnt += 1
    # slow + 1, fast, slow 맞춰줌, total 초기화
    if total == n:
        cnt += 1
        slow += 1
        fast = slow
        total = 0
    # n이 아닌 경우에 slow가 마지막 인덱스이고, fast가 인덱스를 넘어간다면..
    # 20구할 때, slow가 19인 경우...
    else:
        if slow == len(num_lst) - 1 and fast >= len(num_lst):
            break
print(cnt)
