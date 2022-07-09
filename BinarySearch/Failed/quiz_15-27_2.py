import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))
set_array = set(array)

def find_smallest(array, x, start, end, smallest):
    if start > end:
        return smallest

    mid = (start+end)//2
    if array[mid] == x:
        if smallest > mid:
            smallest = mid
            find_smallest(array, x, start, mid-1, smallest)
        else:
            return smallest
    elif array[mid] > x:
        find_smallest(array, x, start, mid-1, smallest)
    else:
        find_smallest(array, x, mid+1, end, smallest)

def find_biggest(array, x, start, end, biggest):
    if start > end:
        return biggest

    mid = (start+end)//2
    if array[mid] == x:
        if biggest < mid:
            biggest = mid
            find_biggest(array, x, start, mid-1, biggest)
        else:
            return biggest
    elif array[mid] > x:
        find_biggest(array, x, start, mid-1, biggest)
    else:
        find_biggest(array, x, mid+1, end, biggest)

if x not in set_array:
    print(-1)
else:
    print(find_biggest(array, x, 0, n-1, 0))
    print(find_biggest(array, x, 0, n-1, 0) - find_smallest(array, x, 0, n-1, n-1) + 1)