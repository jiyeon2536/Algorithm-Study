import sys
input = sys.stdin.readline

N, M = map(int, input().split())

real_dict = dict()

for n in range(N):
    S = input().strip().rstrip()

    if len(S) >= M:
        real_dict.setdefault(S, 0)
        real_dict[S] += 1

result = list(real_dict.keys())

result.sort()
result.sort(key=lambda x: len(x), reverse=True)
result.sort(key=lambda y: real_dict[y], reverse=True)

print(*result, sep="\n")
