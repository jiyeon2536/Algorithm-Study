N = int(input())
rope = []

for _ in range(N):
    rope.append(int(input()))

rope.sort()

mx = 0

for idx in range(N):
    weight = rope[idx] * (N - idx)
    
    if weight > mx:
        mx = weight
        
print(mx)