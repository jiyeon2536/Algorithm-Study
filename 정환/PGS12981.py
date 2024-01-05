def solution(n, words):
    answer = []
    
    cycle = 1
    words_set = set()
    idx = 0
    while idx < len(words):
        if idx != 0 and idx % n == 0:
            cycle += 1
        if words[idx] in words_set:
            answer.append((idx % n + 1))
            answer.append(cycle)
            break
        if idx != 0 and words[idx][0] == words[idx- 1][-1]:
            words_set.add(words[idx])
        elif idx != 0 and words[idx][0] != words[idx - 1][-1]:
            answer.append((idx % n) + 1)
            answer.append(cycle)
            break
        else:
            words_set.add(words[idx % n])
        idx += 1
        
    if answer == []:
        answer = [0, 0]

    return answer
