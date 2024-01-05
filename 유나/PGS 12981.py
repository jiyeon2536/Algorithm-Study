# 이미 나온 단어라면? 앞사람 마지막 글자로 시작하지 않는다면?
def solution(n, words):
    # 탈락자가 발생하지 않았다면 0, 0
    answer = [0, 0]
    check_word = {words[0]:words[0]}
    number = 1
    for idx in range(1, len(words)):
        check = check_word.get(words[idx], False)
        number += 1
        
        # 이전에 나오지 않은 단어 & 이전 단어의 마지막 글자로 시작하는지?
        if not check and words[idx-1][-1] == words[idx][0]:
            check_word.setdefault(words[idx], words[idx])
        else:
            answer = [number % n if number % n else n , number // n if not number % n else number // n + 1]
            break

    return answer
