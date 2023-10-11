import sys
input = sys.stdin.readline
from collections import deque

number_of_members = int(input())
friends = [[] for _ in range(number_of_members + 1)]

while True:
    friend_1, friend_2 = list(map(int, input().split()))
    if friend_1 == -1:
        break
    else:
        friends[friend_1].append(friend_2)
        friends[friend_2].append(friend_1)

candidates = []
mn = 51
for i in range(1, number_of_members + 1):
    far_from_each = [0] * (number_of_members + 1)
    visited = [0] * (number_of_members + 1)
    visited[i] = 1
    connection = deque([i])
    # BFS
    while connection:
        number = connection.popleft()
        for friend in friends[number]:
            if not visited[friend]:
                connection.append(friend)
                visited[friend] = visited[number] + 1
    minus_score = max(visited) - 1
    if minus_score < mn:
        candidates = [i]
        mn = minus_score
    elif minus_score == mn:
        candidates.append(i)

print(mn, len(candidates))
print(*candidates)