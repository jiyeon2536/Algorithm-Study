import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()
for i in range(1, m+1):
    cards[0] += cards[1]
    cards[1] = cards[0]
    cards.sort()
print(sum(cards))