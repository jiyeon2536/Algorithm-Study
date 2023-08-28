T = int(input())

for tc in range(1, T + 1):
    cards = list(input().strip())

    S, D, H, C = [], [], [], []
    
    error = False

    for i in range(len(cards) // 3):
        if cards[i * 3] == 'S':
            if (cards[i * 3 + 1] + cards[i * 3 + 2]) in S:
                error = True
                break
            S.append((cards[i * 3 + 1] + cards[i * 3 + 2]))
        if cards[i * 3] == 'D':
            if (cards[i * 3 + 1] + cards[i * 3 + 2]) in D:
                error = True
                break
            D.append((cards[i * 3 + 1] + cards[i * 3 + 2]))
        if cards[i * 3] == 'H':
            if (cards[i * 3 + 1] + cards[i * 3 + 2]) in H:
                error = True
                break
            H.append((cards[i * 3 + 1] + cards[i * 3 + 2]))
        if cards[i * 3] == 'C':
            if (cards[i * 3 + 1] + cards[i * 3 + 2]) in C:
                error = True
                break
            C.append((cards[i * 3 + 1] + cards[i * 3 + 2]))

    if error == True:
        print(f'#{tc} ERROR')
    else:
        print(f'#{tc} {13 - len(S)} {13 - len(D)} {13 - len(H)} {13 - len(C)}')
