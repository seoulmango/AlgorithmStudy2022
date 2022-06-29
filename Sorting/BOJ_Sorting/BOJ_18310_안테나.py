n = int(input())
hlist = list(map(int, input().split()))

hlist.sort()

if n % 2 == 1:
    print(hlist[n//2])
else:
    left = n//2 - 1
    right = n//2
    l_sum = 0
    r_sum = 0
    for h in hlist:
        l_sum += abs(h - hlist[left])
        r_sum += abs(h - hlist[right])
    if r_sum < l_sum:
        print(hlist[right])
    else:
        print(hlist[left])