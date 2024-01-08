def solution(users, emoticons):
    from itertools import product
    answer = []
    mn = 40
    sale_lst = []
    # 구매 가능 세일 최솟값 구하기
    for user in users:
        mn = min(user[0], mn)
    # 세일 최솟값 이상인 경우만 담은 sale_lst
    for sale in [10, 20, 30, 40]:
        if sale >= mn:
            sale_lst.append(sale)
    mx = [0, 0]
    for price in product(sale_lst, repeat = len(emoticons)):
        # 선택한 할인율로 한바퀴 돌기
        personal = [0, 0]
        for user in users:
            personal_total = 0
            for idx in range(len(emoticons)):
                # 할인이 기준 이상이라면! 구입
                if price[idx] >= user[0]:
                    personal_total += emoticons[idx] * (100-price[idx]) * 0.01
            # 기준 금액 이상이라면
            if personal_total >= user[1]:
                personal[0] += 1
                personal_total -= emoticons[idx] * (100-price[idx]) * 0.01
            else:
                personal[1] += personal_total
        # 돌고난 후에 mx와 비교
        if personal[0] > mx[0]:
            mx[0], mx[1] = int(personal[0]), int(personal[1])
        elif personal[0] == mx[0] and personal[1] >= mx[1]:
            mx[0], mx[1] = int(personal[0]), int(personal[1])
    return mx
