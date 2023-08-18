def rec(idx, res):
    global mn
    global mx

    if idx == N:
        # 결과가 최소 또는 최대일 경우...
        if mn > res:
            mn = res

        if mx < res:
            mx = res

        return

    for i in range(4):
        # '+', '-', '*', '/'이 각각 0 이상 존재하면...
        if operations[i] > 0:
            # 다음 숫자와 연산의 모든 조합을 순회... 
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
                # res가 양수일 경우와 음수일 경우의 연산과정이 다름
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

# 모든 경우의 수 구하기 시작
rec(1, cur_sum)

print(mx)
print(mn)