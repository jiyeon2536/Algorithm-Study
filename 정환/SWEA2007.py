T = int(input())
for tc in range(1, T + 1):
    arr = input()

    arr_list = list(arr)

    queue = []

    while True:
        queue.append(arr_list.pop(0))
        if queue == arr_list[:len(queue)] and queue == arr_list[len(queue): 2 * len(queue)]:
            break

    print(f'#{tc} {len(queue)}')
