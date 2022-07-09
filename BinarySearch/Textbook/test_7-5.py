import sys


n = int(sys.stdin.readline().rstrip())
nlist = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
mlist = list(map(int, sys.stdin.readline().rstrip().split()))

nlist.sort()

def find(m, nlist, start, end):
    mid = (start+end)//2
    if start > end:
        return 'no'
    elif nlist[mid] == m:
        return 'yes'
    elif nlist[mid] > m:
        return find(m, nlist, start, mid-1)
    else:
        return find(m, nlist, mid+1, end)
    
for order in mlist:
    print(find(order, nlist, 0, n-1), end=" ")