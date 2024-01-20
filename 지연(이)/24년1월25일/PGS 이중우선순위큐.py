import heapq
def solution(operations):
    answer = []
    min_heap = []
    max_heap = []
    d = dict()
    for oper in operations:
        str1,str2 = oper.split()
        if str1=='I':
            heapq.heappush(min_heap, int(str2))
            heapq.heappush(max_heap, -int(str2))
            if int(str2) in d.keys():
                d[int(str2)]+=1
            else:
                d[int(str2)] = 1

        else:
            if str2=='-1':
                while min_heap:
                    if min_heap[0] in d.keys():
                        value = heapq.heappop(min_heap)
                        d[value]-=1
                        if d[value]==0:
                            d.pop(value)
                        break
                    else:
                        heapq.heappop(min_heap)
            else:
                while max_heap:
                    if -max_heap[0] in d.keys():
                        value = heapq.heappop(max_heap)
                        d[-value]-=1
                        if d[-value]==0:
                            d.pop(-value)
                        break
                    else:
                        heapq.heappop(max_heap)
        # print(d, min_heap, max_heap)
                

    if d:
        mn = float('inf')
        mx = 0
        for key in d.keys():
            if mn>key:
                mn = key
            if mx<key:
                mx = key
        answer = [mx,mn]
    else:
        answer = [0,0]

        
    return answer
