def magnetic(arr):
    # 한 줄 씩 교착 상태의 수를 파악
    deadlock_num = 0

    is_n = False

    for n in range(100):
        # n극에서 s극 쪽으로 선형 탐색하다가 n을 만나면 기록
        if arr[n] == 1:
            is_n = True

        # 이전에 n이 있었고 탐색 중에 s를 만나면 교착 상태!
        if arr[n] == 2 and is_n:
            deadlock_num += 1
            # 교착 상태에 빠진 n은 이제 기록되지 않음
            is_n = False

    return deadlock_num

T = 10

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N = int(input())
    not_table = [list(map(int, input().split())) for _ in range(N)]
    # 왼쪽이 N극... N극 성질의 자성체는 1
    # 오른쪽이 S극... S극 성질의 자성체는 2
    table = list((map(list, zip(*not_table))))

    # 교착 상태를 모두 더한 값
    total_deadlock_num = 0

    for line in table:
        total_deadlock_num += magnetic(line)

    print(total_deadlock_num)