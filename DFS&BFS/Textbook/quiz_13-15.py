from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
roads = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cities = [-1]*(n+1)
cities[x] = 0

queue = deque([x])

while queue:
    now = queue.popleft()
    for next_city in graph[now]:
        if cities[next_city] == -1:
            cities[next_city] = cities[now] + 1
            queue.append(next_city)

check = False
for i in range(1, n+1):
    if cities[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
