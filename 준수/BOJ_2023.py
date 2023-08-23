# 일의 자리에 수가 들어와도 소수인지 판별
def recursion(depth, dpd):
    # 수의 길이가 N일 경우 재귀 중단
    if depth == N:
        print(dpd)
        return

    # 일의 자리를 비워주자
    gk = dpd * 10

    # 10의 배수는 소수가 이님
    for idx in range(1, 10):
        # 일의 자리에 1부터 9까지 붙여보고 소수라면 다음 재귀로!
        tmp = gk + idx

        if is_prime(tmp):
            recursion(depth + 1, tmp)


# 소수 판별 알고리즘 (에라토스 테네스의 체)
def is_prime(num):
    # 1은 소수가 아님
    if num == 1:
        return False

    # 해당 숫자의 제곱근
    m = int(num ** 0.5)
    # 과연 소수인가?
    is_true = True

    # 1이 아닌 제곱근 이하의 수로 나누어지지 않으면 소수
    for mod in range(2, m + 1):
        if num % mod == 0:
            is_true = False

    return is_true


N = int(input())

# 가장 앞 자리는 0이 될 수 없고 소수여야 함
for glgl in range(1, 10):
    # 만약 앞 자리가 소수라면
    if is_prime(glgl):
        # 다음 자리부터 재귀
        recursion(1, glgl)