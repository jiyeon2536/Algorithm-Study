T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    string = input()

    word_list = []
    tmp_str = ''

    for i in range(10):
        tmp_str += string[i]
        word_list.append(tmp_str)

    result = 0

    for length in range(1, 10):
        is_cont = True

        for k in range(0, 30 - length, length):
            if not is_cont:
                break

            for m in range(length):
                if word_list[length][m] != string[m + k]:
                    is_cont = False
                    break

        if is_cont:
            result = length
            break
            
    print(result)