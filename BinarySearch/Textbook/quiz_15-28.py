import sys

n = int(sys.stdin.readline().rstrip())
nlist = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = n-1

while start <= end:
    mid = (start+end) //2
    if nlist[mid] == mid:
        print(mid)
        break
    elif nlist[mid]<mid:
        start = mid+1
    else:
        end = mid-1
else:
    print(-1)