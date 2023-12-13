def comb(arr, collected):
    new_collected = collected[:]

    # 숫자 6개만 뽑는다...
    if len(arr) == 6:
        print(*arr)
        return
    
    for idx in range(length):
        if new_collected[idx] == False:
            # 다음 숫자를 뽑을 때 앞의 숫자는 고려하지 않음
            new_collected[idx] = True
            comb(arr + [numbers[idx]], new_collected)


while True:
    length, *numbers = map(int, input().split())
    # 사전 순으로 정렬
    numbers.sort()
    
    # 입력이 0일 때 중지
    if not length:
        break

    # 중복 제거
    collected = [False] * length
    comb([], collected)
    print()