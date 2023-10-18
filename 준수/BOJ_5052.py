class Node:
    def __init__(self, data):
        self.data = data
        self.next = [None] * 10


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = []

    for _ in range(N):
        number = list(map(int, input()))
        numbers.append(number)

    numbers.sort(key=lambda x: -len(x))

    is_consistency = True
    root_node = Node(None)

    for number in numbers:
        now_node = root_node

        if not is_consistency:
            break

        for idx in range(len(number)):
            temp = number[idx]

            if now_node.next[temp]:
                if idx == len(number) - 1:
                    is_consistency = False
                    break

                now_node = now_node.next[temp]
            else:
                now_node.next[temp] = Node(temp)
                now_node = now_node.next[temp]

    if is_consistency:
        print('YES')
    else:
        print('NO')
