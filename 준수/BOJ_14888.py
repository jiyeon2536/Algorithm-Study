def rec(idx, res):
    global mn
    global mx

    if idx == N:
        if mn > res:
            mn = res

        if mx < res:
            mx = res

        return

    for i in range(4):
        if operations[i] > 0:
            if i == 0:
                operations[i] -= 1
                rec(idx + 1, res + numbers[idx])
                operations[i] += 1

            if i == 1:
                operations[i] -= 1
                rec(idx + 1, res - numbers[idx])
                operations[i] += 1

            if i == 2:
                operations[i] -= 1
                rec(idx + 1, res * numbers[idx])
                operations[i] += 1

            if i == 3:
                operations[i] -= 1
                if res >= 0:
                    rec(idx + 1, res // numbers[idx])
                else:
                    rec(idx + 1, -(-res // numbers[idx]))
                operations[i] += 1


N = int(input())
numbers = list(map(int, input().split()))
operations = list(map(int, input().split()))

cur_sum = numbers[0]

mn = 1000000000
mx = -1000000000

rec(1, cur_sum)

print(mx)
print(mn)