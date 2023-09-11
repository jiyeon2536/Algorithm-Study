N = int(input())

# 0 이하의 수를 담는 배열
negative = []
# 1 이상의 수를 담는 배열
positive = []

res = 0

# case work
for _ in range(N):
    number = int(input())

    # 음수를 그냥 더하는 것보다 0을 곱하면 더 높은 수가 되기 때문
    if number > 0:
        positive.append(number)
    else:
        negative.append(number)

# 상황에 맞게 정렬
negative.sort(reverse=True)
positive.sort()

# 음수와 0이 담긴 배열부터 그리디로 접근
while len(negative) > 1:
    a = negative.pop()
    b = negative.pop()

    res += max(a * b, a + b)

# 다음은 0을 제외한 양수가 담긴 배열
while len(positive) > 1:
    a = positive.pop()
    b = positive.pop()

    res += max(a * b, a + b)

# 두 배열에서 수가 하나씩 남았다면
if negative and positive:
    a = negative.pop()
    b = positive.pop()

    res += max(a * b, a + b)
# 두 배열 중 하나만 수가 남을 경우
elif negative:
    res += negative.pop()
elif positive:
    res += positive.pop()

print(res)