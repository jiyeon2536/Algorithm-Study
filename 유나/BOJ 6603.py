# n개 중 6개를 뽑는 조합 함수
# n : 총 개수, r : 뽑아야할 남은 개수, S : 시작 인덱스
def ncr(n, r,s):
    # 원하는 만큼 다 뽑았다면
    if r == 0:
        # 역순으로 출력
        print(*(reversed(res)))
        return
    # s부터 n - r + 1까지
    for i in range(s, n - r + 1):
        # r-1에 i번째 값 입력
        res[r-1] = arr[i] 
        # 재귀
        ncr(n, r-1, i+1)
    
# 참인 동안에 k, arr 입력받음
while True:
    k, *arr = list(map(int, input().strip().split())) 
    
    # k가 0이라면 break
    if k == 0:
        break   
    
    # 결과받을 res 생성
    res = [0] * 6
    ncr(k, 6, 0)
    print()
