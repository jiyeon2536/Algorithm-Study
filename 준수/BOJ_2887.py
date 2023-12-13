import heapq


def find(c):
    if parent[c] == c:
        return c

    parent[c] = find(parent[c])
    return parent[c]


def union(c1, c2):
    c1 = find(c1)
    c2 = find(c2)

    if c1 > c2:
        parent[c1] = c2
    else:
        parent[c2] = c1


N = int(input())
planets = []
parent = [_ for _ in range(N)]

for num in range(N):
    x, y, z = map(int, input().split())
    planets.append((num, x, y, z))

edges = []

for coord in range(1, 4):
    planets.sort(key=lambda k: k[coord])

    for idx in range(N - 1):
        planet = planets[idx]
        next_planet = planets[idx + 1]

        dist = abs(planet[coord] - next_planet[coord])

        heapq.heappush(edges, (dist, planet[0], next_planet[0]))

mn_cost = 0

while edges:
    dist, start, end = heapq.heappop(edges)

    if find(start) != find(end):
        union(start, end)
        mn_cost += dist

print(mn_cost)