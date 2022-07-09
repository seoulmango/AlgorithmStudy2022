# 0423 0431

import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
hlist = list(map(int, sys.stdin.readline().rstrip().split()))

hlist.sort()

start = 0
end = hlist[-1]
ans = 0
mid = (start + end)//2

while start <= end:
    total = 0
    for h in hlist:
        if mid < h:
            total += h - mid
    if total >= m:
        ans = mid
        start = mid+1
        mid = (start+end)//2
    elif total < m:
        end = mid-1
        mid = (start+end)//2

print(ans)