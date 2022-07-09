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

# 틀렸던 이유: 작은 것 두 개의 합이 3번째+4번째로 작은 수의 합보다 더 큰 수가 될 수도 있다..!
# ex) 5, 50, 51, 52 순으로 있을 때
# 5+50이 51+52보다 커진다. 그러므로 위의 코드는 올바르지 못하다.