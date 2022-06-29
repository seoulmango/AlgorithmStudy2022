import heapq

n = int(input())
nlist=[]
for _ in range(n):
   heapq.heappush(nlist, int(input()))
ans = 0
while len(nlist) != 1:
    x = heapq.heappop(nlist)
    y = heapq.heappop(nlist)
    ans += x + y
    heapq.heappush(nlist, x+y)
print(ans)