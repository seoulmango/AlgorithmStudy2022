import sys
input = sys.stdin.readline

w, m, k = map(int, input().split())

count = 0

while True:
    w -= 2
    m -= 1
    count += 1

    if w < 0 or m < 0:
        count -= 1
        w += 2
        m += 1
        break

    elif w == 0 or m == 0:
        break

if w+m >= k:
    print(count)
else:
    while True:
        count -= 1
        k -= 3
        if w+m >= k:
            break
        elif count == 0:
            break
    print(count)