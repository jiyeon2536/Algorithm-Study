# 16953 A -> B

A, B = map(int, input().split())

result = 1
while True:
    if B % 2 == 1:
        B = (B - 1) / 10
        result += 1
    else:
        B /= 2
        result += 1
    if B == A:
        break
    elif B < A:
        result = -1
        break
print(result)
