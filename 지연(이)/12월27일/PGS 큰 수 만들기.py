def find_ch(number, pick,cnt):
    # print(number,pick)
    for i in range(9,-1,-1):
        if not cnt[i]:
            continue
        for j in range(len(number)-pick+1):
            if number[j]==str(i):
                cnt[i]-=1
                return str(i), j
    return 'error', -1

            
def solution(number, k):
    answer = ''
    cnt = [0]*10
    for n in number:
        cnt[int(n)]+=1
    
    idx = 0
    pick = len(number)-k
    while pick:
        if pick==len(number):
            answer += number
            pick-=len(number)
            break
        num, idx = find_ch(number, pick,cnt)
        answer += num
        number = number[idx+1:]
        pick-=1
        # print(pick, number, num)
    return answer
