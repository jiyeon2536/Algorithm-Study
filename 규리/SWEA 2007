T = int(input())
for tc in range(1, T+1):
    txt = input()
    f = txt[0]

    for i in range(2, len(txt)):
        if txt[i] == f and txt[0:i] == txt[i:2*i]:
            result = i
            break

    print(f'#{tc} {result}')
