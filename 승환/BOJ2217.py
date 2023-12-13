N = int(input())
arr = []
for i in range(N):
    w = int(input())  
    arr.append(w)
arr.sort() # 오름차순으로 정렬한다.
sv = 0 
mx = 0
for i in range(N):
    sv = arr[i] * (N - i)  # 하나씩 빼면서 곱으로 계산한다.
    mx = max(sv, mx)
print(mx)
