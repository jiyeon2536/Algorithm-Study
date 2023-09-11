def f(k):
    if k == L:
        cnt = 0
        if 97 or 101 or 105 or 111 or 117 in ans:  # 모음이면 더해라
            cnt += ans.count(97)  # a 가 있으면
            cnt += ans.count(101)  # e
            cnt += ans.count(105)  # i
            cnt += ans.count(111)  # o
            cnt += ans.count(117)  # u
            if cnt < 1 or k - cnt < 2:  # 모음이 0개거나 자음이 두개 미만일때(모음 0개는 셀 필요 없다.)
                return
        else:
            return
        for j in range(L):
            print(chr(ans[j]), end='')
        print()
        return
    for r in range(k, C):
        if wor[r] not in ans:  # 중복 방지
            if ans:  # 안에 값이 있을 때
                if ans[-1] < wor[r]:  # 그 값보다 커야함
                    ans.append(wor[r])
                else:
                    continue
            else:  # 없으면 그냥 추가
                ans.append(wor[r])
        else:
            continue
        f(k+1)
        ans.pop()


L, C = map(int, input().split())
arr = list(input().split())
# ord함수를 써서 증가하는지 확인해야 한다.
# 최소 한개의 모음과 두개의 자음으로 이루어져 있다.
# 자음과 모음을 확인하고, 구분한다.
wor = []
ans = []
for i in range(C):
    #if arr[i] in {'a', 'e', 'i', 'o', 'u'}:
    s = ord(arr[i])  # 모음이랑 자음 크기도 비교해야하기 때문에
    wor.append(s)
    #else:
    #    s = ord(arr[i])
    #    vow.append(s)
wor.sort()
f(0)
