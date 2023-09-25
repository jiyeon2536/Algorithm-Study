import sys
input = sys.stdin.readline

s = input().strip()
t = list(input().strip())

n = len(s)
ans = 0

# s가 모두 A와 B로 이루어져 있는지 체크
cnt_s = 0
for i in s:
    if i in ['A', 'B']:
        cnt_s += 1

# t가 모두 A와 B로 이루어져 있는지 체크
cnt_t = 0
for i in t:
    if i in ['A', 'B']:
        cnt_t += 1

# s와 t가 모두 A와 B로 이루어져 있다면
if cnt_t == len(t) and cnt_s == len(s):
  # 역순으로 체크
    for i in range(len(t)-1, -1, -1):
        if len(t) == n:
            if ''.join(t) == s:
                ans = 1
                break
        # B이면 pop하고, reverse
        if t[i] == 'B':
            t.pop()
            t.reverse()
        # A이면 pop
        elif t[i] == 'A':
            t.pop()
        else:
            break

print(ans)
