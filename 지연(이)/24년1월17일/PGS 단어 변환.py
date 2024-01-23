import heapq

def solution(begin, target, words):
    if target not in words:
        return 0
    
    N = len(begin)
    h = []
    diff = 0
    for i in range(N):
        if begin[i]!=target[i]:
            diff+=1
    heapq.heappush(h,(diff, begin, 0))
    
    while h:
        now_diff, now_word, now_step = heapq.heappop(h)
        if now_word == target:
            return now_step
        
        # nxt_word append
        # nxt_word 특징 : nxt_step = now_step+1,now_word 1글자 다름, diff는 nxt_word와 target가 다른 정도
        for nxt_word in words:
            now_nxt_diff, nxt_tar_diff = 0, 0
            for i in range(N):
                if now_word[i] != nxt_word[i]:
                    now_nxt_diff+=1
                if nxt_word[i] != target[i]:
                    nxt_tar_diff+=1
            if now_nxt_diff==1:
                heapq.heappush(h, (nxt_tar_diff, nxt_word, now_step+1))
        
    return 0
