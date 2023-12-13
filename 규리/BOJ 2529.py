import sys
from itertools import permutations
input = sys.stdin.readline

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
N = int(input())
txt = input().split()

perm_list = list(permutations(num, N+1))

ans = []
for i in range(len(perm_list)):
    check = True
    for j in range(N):
        if txt[j] == '<' and perm_list[i][j] >= perm_list[i][j+1]:
            check = False
        if txt[j] == '>' and perm_list[i][j] <= perm_list[i][j+1]:
            check = False
    if check == True:
        ans.append(''.join(map(str, perm_list[i])))

print(max(ans))
print(min(ans))
