S = input()
T = input()

while len(T) > len(S):
    length = len(T)
    if T[-1] == 'A':
        T = T[:length-1]
    elif T[-1] == 'B':
        T = T[:length-1][::-1]
    else:
        break

if T != S:
    print(0)
else:
    print(1)
