import sys

n, c = map(int, sys.stdin.readline().rstrip().strip())
hlist = []
for _ in range(n):
    hlist.append(int(sys.stdin.readline().rstrip()))
hlist.sort()

start = 0
end = n-1
cameras = [start, end]
while len(cameras) != c:
    if (start+end)%2 == 0:
        mid = (start+end)/2
    else:
        a = hlist[(start+end)//2] - hlist[start]
        b = hlist[end] - hlist[((start+end)//2)+1]
        if a>b:
            mid = (start+end)//2
        else:
            mid = ((start+end)//2)+1
    cameras.append(mid)
    
