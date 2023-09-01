import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 단어개수, 단어길이기준
words = {}
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

lst = []
for k in words.keys():
    lst.append([words[k], k])

lst.sort(key=lambda x:(-x[0], -len(x[1]), x[1]))

for i in range(len(lst)):
    print(lst[i][1])
