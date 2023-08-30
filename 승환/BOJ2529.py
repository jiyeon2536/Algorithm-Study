n = int(input())
s = list(input().split())
mx = []
mn = []
mx_lst = [i for i in range(10)]
mn_lst = [i for i in range(10)]
cnt = 0
mx_stack = []
for i in range(len(s)):  # 최댓값 구하기
    if s[i] == '<':
        mx_stack.append('<')  # stack ++
    elif s[i] == '>':
        mx_stack.append('>')  # 이걸 만나면 최댓값이 확정된다.
        while mx_stack:  # < 이걸 추가해 준 만큼
            mx.append(mx_lst.pop(len(mx_lst) - len(mx_stack)))  # < 추가해놓은 것 만큼 작은 값이 들어간다.
            mx_stack.pop()
if mx_stack:
    while mx_stack:  # < 남아 있는경우
        mx.append(mx_lst.pop(len(mx_lst) - (len(mx_stack)+1)))  # 추가한다.
        mx_stack.pop()
mx.append((mx_lst.pop()))

mn_stack = []  # 최솟값 구하기
for i in range(len(s)):
    if s[i] == '>':  # 값이 확정되지 않아 추가한다.
        mn_stack.append('>')
    elif s[i] == '<':   # 값이 확정된다.
        mn_stack.append('<')
        while mn_stack:  # > 갯수만큼 낮은 값을 넣는다.
            mn.append(mn_lst.pop(len(mn_stack)-1))
            mn_stack.pop(0)
if mn_stack:  # >가 남아있으면
    while mn_stack:  #추가하낟.
        mn.append(mn_lst.pop(len(mn_stack)))
        mn_stack.pop(0)
mn.append((mn_lst.pop(0)))
res1 = ''
for i in range(len(mx)):  # 출력
   res1 += str(mx[i])
print(res1)
res2 = ''
for j in range(len(mn)):
    res2 += str(mn[j])
print(res2)
