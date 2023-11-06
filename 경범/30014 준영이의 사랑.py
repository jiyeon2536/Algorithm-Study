
# 메인 로직

def sor():
    pass
# 인풋
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

test1 =[]
test2 = []
for x in range(1, len(arr)):
    if x % 2 == 0:
        test1.append(arr[x])
    else:
        test2.append(arr[x])
test1.sort(reverse=True)
test3 = [arr[0]] + test2 + test1
cnt1 = 0
for j in range(len(test3)):
    if j != len(test3) - 1:
        cnt1 += test3[j] * test3[j + 1]
    else:
        cnt1 += test3[j] * test3[0]

# 아웃풋

print(cnt1)
print(*test3)


