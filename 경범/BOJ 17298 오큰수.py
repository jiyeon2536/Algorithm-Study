# 메인 로직

def fun():
    stack = []
    for i in range(n):
        if stack:
            if stack[-1][1] >= arr[i]:
                stack.append([i, arr[i]])
            else:
                while stack:
                    if stack[-1][1] >= arr[i]:
                        break
                    index, a = stack.pop()
                    total[index] = arr[i]
                stack.append([i, arr[i]])

        else:
            stack.append([i, arr[i]])



# 인풋

n = int(input())
arr = list(map(int, input().split()))
total = [-1] * n

fun()
# 아웃풋
print(*total)
