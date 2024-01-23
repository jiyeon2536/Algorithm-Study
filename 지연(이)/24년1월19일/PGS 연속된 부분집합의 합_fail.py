def solution(sequence,k):
    N = len(sequence)
    result = [N,N+N]
    
    # 생각나는 방법이 없어
    # combination 2개를 선택해야하니깐
    
    # if문에서 초과되진 않을꺼야
    # 그럼 이중for문인데
    # 어떻게 해결할 수 있을까
    # 생각나는 방법이 없어
    
    # combination 2개 선택 말고 다른 방법이 있을까
    # 한번에 연산해서 답을 찾는 방법은 있을까?
    # combination 2개 선택 이중for문, 재귀, 비트 연산?
    
    # 내가 푼 적이 있는데
    for i in range(N):
        Sum = 0
        for j in range(i,N):
            Sum += sequence[j]
            # print((i,j), (Sum, sum(sequence[i:j+1])))
            if Sum==k:
                if result[1]-result[0] > j-i:
                    result = [i,j]
                elif result[1]-result[0] == j-i:
                    if i<result[0]:
                        result = [i,j]
        Sum-=sequence[i]
    return result
