S = list(input())
T = list(input())

# 반대로 접근
while len(S) < len(T):
    # 뒤에서 'A'를 뺄 수 있냥
    if T[-1] == 'A':
        T.pop()
    # 뒤에서 'B'를 뺄 수 있냥
    elif T[-1] == 'B':
        T.pop()
        # 그럼 뒤집어!
        T = T[::-1]

# 같냥?
if S == T:
    print(1)
else:
    print(0)