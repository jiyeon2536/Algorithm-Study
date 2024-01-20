import heapq
def solution(n, works):
    def min_work(n,works):
        h = []
        for w in works:
            heapq.heappush(h, -w)
        
        while h and n:
            v = -heapq.heappop(h)
            if v==0:
                break
            v -= 1
            n -= 1
            heapq.heappush(h, -v)
        return h

    lst=min_work(n,works)
    answer = 0
    for i in lst:
        answer += i**2
    return answer
