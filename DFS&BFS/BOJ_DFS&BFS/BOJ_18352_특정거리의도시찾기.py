import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]
distance = [-1 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)

distance[x] = 0
queue = deque([x])
while queue:
    v = queue.popleft()
    for i in graph[v]:
        if distance[i] == -1:
            distance[i] = distance[v] + 1
            queue.append(i)

if k not in distance:
    print(-1)
else:
    for i in range(len(distance)):
        if distance[i] == k:
            print(i)