from collections import deque

n, m, k, x = map(int, input().split())

road = [[] for _ in range(n+1)]

# 인접 리스트
for _ in range(m):
    city_idx1, city_idx2 = map(int, input().split())
    road[city_idx1].append(city_idx2)

# x로부터의 거리
dlist = [-1 for _ in range(n+1)]
dlist[x] = 0

queue = deque([x])

while queue:
    v = queue.popleft()
    for nextcity in road[v]:
        if dlist[nextcity] == -1:
            dlist[nextcity] = dlist[v] + 1
            queue.append(nextcity)

check = False
for i in range(1, len(dlist)):
    if dlist[i] == k:
        print(i)
        check = True
if not check:
    print(-1)