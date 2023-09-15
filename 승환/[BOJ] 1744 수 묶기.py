N = int(input())
arr1 = []
zero = []  # 0이면 여기에 담아라
arr2 = []
for i in range(N):
    s = int(input())
    if s == 0:
        zero.append(s)
    else:
        if s > 0:
            arr1.append(s)
        else:
            arr2.append(s)
arr1.sort()
arr2.sort()
len_arr1 = len(arr1)
len_arr2 = len(arr2)
sv = 0
temp = 0
if len_arr1 >= 2:
    if len_arr1 % 2 == 0:
        for i in range(0, len_arr1, 2):
            if arr1[i] > 1 and arr1[i+1] > 1:
                sv += arr1[i] * arr1[i+1]
            else:
                sv += arr1[i] + arr1[i+1]
    else:  # 홀수 개인 경우 제일 작은 값은 따로 더한다.
        for i in range(1, len_arr1, 2):
            if arr1[i] > 1 and arr1[i + 1] > 1:
                sv += arr1[i] * arr1[i+1]
            else:
                sv += arr1[i] + arr1[i+1]
        sv += arr1[0]
else:  # 양수가 1개일 때
    if arr1:
        sv += arr1[0]
if len_arr2 >= 2:
    if len_arr2 % 2 == 0:
        for i in range(0, len_arr2, 2):
            sv += arr2[i] * arr2[i+1]
    else:  # 홀수 개인 경우 제일 작은 값은 따로 더한다.
        for i in range(0, len_arr2-1, 2):
            sv += arr2[i] * arr2[i + 1]
        temp = arr2[-1]
else:  # 음수가 1개 이하일 때
    if len(zero) > 0:
        sv += 0
    else:
        if arr2:
            sv += arr2[0]
if len(zero) > 0 and temp != 0:
    sv += 0
else:
    sv += temp
print(sv)
