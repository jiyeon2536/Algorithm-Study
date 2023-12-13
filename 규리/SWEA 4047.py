T = int(input())
for tc in range(1, T+1):
    C = input()
    card = []
    alpha = []
    for i in range(0,len(C),3):
        card.append(C[i:i+3])
        alpha.append(C[i])
    card2 = list(set(card))

    if card != card2:
        print(f'#{tc} ERROR')
        continue

    result = []
    for i in 'SDHC':
        result.append(13-alpha.count(i))
    print(f'#{tc}', *result)
