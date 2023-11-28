import sys
from collections import deque
input = sys.stdin.readline
# 메인 로직

def sor():
    global total
    cnt = total
    for i in range(n):
        start = i
        end = (k + i) % n
        current[sushi[start]] -= 1
        if current[sushi[start]] == 0:
            cnt -= 1
        if sushi[end] not in current:
            cnt += 1
            current[sushi[end]] = 1
        else:
            if current[sushi[end]] == 0:
                cnt += 1
                current[sushi[end]] += 1
            else:
                current[sushi[end]] += 1
        total = max(cnt, total)



# 인풋
n, d, k, c = map(int, input().split())
sushi = []

for _ in range(n):
     sushi.append(int(input()))
total = 0
current = {}
current[c] = 1
total += 1

for i in range(k):
    if sushi[i] not in current:
        current[sushi[i]] = 1
        total += 1
    else:
        current[sushi[i]] += 1


# 아웃풋
sor()
print(total)
