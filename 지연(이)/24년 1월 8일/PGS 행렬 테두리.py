def solution(N, M, queries):
    answer = []
    arr = [[((i)*M+j+1) for j in range(M) ] for i in range(N) ]
    
    def func(x1,y1,x2,y2,pre_arr):
        mn = pre_arr[x1][y2]
        
        # x1
        for j in range(y2,y1,-1):
            if mn>pre_arr[x1][j-1]:
                mn = pre_arr[x1][j-1]
            pre_arr[x1][j], pre_arr[x1][j-1] = pre_arr[x1][j-1],pre_arr[x1][j]
        
        # y1
        for i in range(x1,x2,+1):
            if mn>pre_arr[i+1][y1]:
                mn = pre_arr[i+1][y1]
            pre_arr[i][y1], pre_arr[i+1][y1] = pre_arr[i+1][y1], pre_arr[i][y1]
        
        # x2
        for j in range(y1,y2,+1):
            if mn>pre_arr[x2][j+1]:
                mn = pre_arr[x2][j+1]
            pre_arr[x2][j], pre_arr[x2][j+1] = pre_arr[x2][j+1],pre_arr[x2][j]
        
        # y2
        for i in range(x2,x1+1,-1):
            if mn>pre_arr[i-1][y2]:
                mn = pre_arr[i-1][y2]
            pre_arr[i][y2], pre_arr[i-1][y2] = pre_arr[i-1][y2], pre_arr[i][y2]
            
        return mn, pre_arr
    
    for x1,y1,x2,y2 in queries:
        mn, arr = func(x1-1,y1-1,x2-1,y2-1,arr)
        answer.append(mn)
    return answer
