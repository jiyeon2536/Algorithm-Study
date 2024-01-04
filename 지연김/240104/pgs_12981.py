# 영어 끝말잇기
def solution(n, words):
    answer = [0, 0]
    spoken = {}
    nth_person = 0
    nth_turn = [1 for _ in range(n)]
    last_char = ''
    
    arr_len = len(words)
    
    # n으로 나눠서 나머지로 사람 구분하기
    for i in range(arr_len):
        word = words[i]
        nth_person = (i % n)
        nth_turn[nth_person] += 1
        
        if (word in spoken) or (i != 0 and (word[0] != last_char)):
            answer[0] = nth_person + 1
            answer[1] = nth_turn[nth_person] -1
            break
            
        last_char = word[-1]
        spoken[word] = 1
        
    return answer