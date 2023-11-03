N = int(input())
S = [0] * 30
S[0] = 3

max_moo = 0

while N > S[max_moo]:
    S[max_moo + 1] = 2 * S[max_moo] + (max_moo + 4)
    max_moo += 1

answer = ''

while max_moo >= 0:
    if S[max_moo - 1] < N <= (max_moo + 3) + S[max_moo - 1]:
        temp = N - S[max_moo - 1]

        if temp == 1:
            answer = 'm'
        else:
            answer = 'o'

        break
    else:
        if N > (max_moo + 3) + S[max_moo - 1]:
            N -= (max_moo + 3) + S[max_moo - 1]

        max_moo -= 1

print(answer)