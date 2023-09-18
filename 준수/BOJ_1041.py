N = int(input())
dice = list(map(int, input().split()))

if N == 1:
    print(sum(dice) - max(dice))
else:
    # 주사위의 특징
    # 반대편과 이어지지 않기 때문에 그 두 가지의 값을 비교함
    nums = sorted([min(dice[0], dice[5]), min(dice[1], dice[4]), min(dice[2], dice[3])])
    first = nums[0]
    second = nums[0] + nums[1]
    third = sum(nums)

    # 꼭지점 4개는 3개의 면이 존재
    vertex = third * 4
    
    # 상단 면에 속한 4개의 변과 옆에 속한 4개의 변의 길이는 다르며
    # 주사위 두 개의 면으로 구성
    edge =  second * (N - 1) * 4 + second * (N - 2) * 4
    
    # 상단 면과 옆면 4개의 크기는 다르며 주사위의 1면들로 구성
    plane = first * (N - 2) * (N - 1) * 4 + first * (N - 2) * (N - 2)

    print(vertex + edge + plane)