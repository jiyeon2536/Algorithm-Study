import sys
input = sys.stdin.readline

N = int(input())  # 회의의 수
lst = [tuple(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x:(x[1], x[0]))

S, E = lst[0]
cnt = 1
for i in range(1, len(lst)):
    start, end = lst[i]
    if E <= start:
        S, E = start, end
        cnt += 1
print(cnt)
