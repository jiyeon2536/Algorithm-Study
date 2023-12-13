X, Y, D, T = map(int, input().split())

jump_move = D / T
dist = ((X * X) + (Y * Y)) ** 0.5

if jump_move > 1:
    answer = dist
    jump_times = 0

    while D * jump_times <= 2 * dist:
        temp_dist = dist - (D * jump_times)
        temp_time = abs(temp_dist) + (jump_times * T)

        if temp_dist < D * 2:
            temp_time = min(abs(temp_dist), T * 2) + (jump_times * T)

        answer = min(answer, temp_time)
        jump_times += 1

    print(answer)
else:
    print(dist)

