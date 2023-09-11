'''
최대 합을 구하기 위한 수 묶기 규칙
1. 2 이상인 수인 경우 가장 큰 수 부터 가능한 만큼 묶어주기
2. 1인 경우 곱하지 않고 그대로 더해주기 (1을 곱해도 그대로이기 때문에 묶지 않고 더해주는 것이 낫다.)
3. 음수인 경우 음수와 음수가 곱하면 양수가 되기 때문에 가장 작은 수부터 가능한 만큼 묶어준다.
4. 0 인 경우 음수와 곱하여 음수로 인해 빠지는 값이 작도록 한다.
'''

import sys
input  = sys.stdin.readline

n =  int(input().strip())

# 최종 합을 구하기 위한 total, 0의 개수를 세는 cnt
total = cnt = 0
# 2이상의 수를 받는 arr_big, 음수를 받는 arr_small
arr_big = []
arr_small = []

# n번 순회하면서
for _ in range(n):
    num = int(input().strip())
    # 입력되는 숫자가 2 이상이면 arr_big에
    # 1 이라면 그대로 total에 더해주기
    # 0 이라면 cnt += 1
    # 음수라면 arr_small에
    if num >= 2:
        arr_big.append(num)
    elif num == 1:
        total += 1
    elif num == 0:
        cnt += 1
    else:
        arr_small.append(num)

# arr_big, arr_sort 정렬
arr_big.sort()
arr_small.sort()

# 음수가 한 개 초과라면 가장 작은 수 부터 두개를 뽑아 묶은 뒤 total에 더해줌
while len(arr_small) > 1:
    a = arr_small.pop(0)
    b = arr_small.pop(0)
    total += a*b

# 수열에 0이 존재하면 그만큼 음수 제거
arr_small = arr_small[cnt:]

# arr_small에 아직 존재한다면, 그 값을 total에 더해준다.
if arr_small:
    total += arr_small[0]

# 2 이상의 숫자가 한개 초과라면 가장 큰 수부터 두개를 뽑아 묶은 뒤 total에 더해줌
while len(arr_big) > 1:
    a = arr_big.pop()
    b = arr_big.pop()
    total += a*b

# 남아 있다면 total에 더해주기
if arr_big:
    total += arr_big[0]

print(total)
