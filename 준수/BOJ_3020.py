def upper_bound(arr, key):
    low = 0
    high = N // 2 - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= key:
            low = mid + 1
        else:
            high = mid - 1

    return high + 1


N, H = map(int, input().split())

above = []
below = []

for idx in range(1, N + 1):
    obstacle = int(input())

    if idx % 2 == 1:
        below.append(obstacle)
    else:
        above.append(obstacle)

above.sort(reverse=True)
below.sort(reverse=True)

height = [0] * (H + 1)

for i in range(1, H + 1):
    below_res = upper_bound(below, i)
    above_res = upper_bound(above, i)
    height[i] += below_res
    height[H - i + 1] += above_res

min_obstacle_num = 200000
min_path_num = 0

for i in range(1, H + 1):
    obstacle_num = height[i]

    if min_obstacle_num > obstacle_num:
        min_obstacle_num = obstacle_num
        min_path_num = 1
    elif min_obstacle_num == obstacle_num:
        min_path_num += 1

print(min_obstacle_num, min_path_num)