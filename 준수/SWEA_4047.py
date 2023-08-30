T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    card = input()
    # 초기 카드의 개수
    cards = {'S': 13, 'D': 13, 'H': 13, 'C': 13}

    is_error = False
    young_joon = []

    for idx in range(0, len(card), 3):
        # 뽑은 카드의 문양 -1
        cards[card[idx]] -= 1

        # 카드 문양과 번호를 임시 문자열에 저장
        tmp_str = ''

        for three in range(3):
            tmp_str += card[idx + three]

        if tmp_str in young_joon:
            # 카드가 겹치면 에러!
            is_error = True
            break
        else:
            # 겹치지 않으면 영준이의 손으로 append
            young_joon.append(tmp_str)

    if is_error:
        print('ERROR')
    else:
        res = []

        # 딕셔너리를 순회하면서 필요한 카드 수 출력
        for value in cards.values():
            res.append(value)

        print(*res)