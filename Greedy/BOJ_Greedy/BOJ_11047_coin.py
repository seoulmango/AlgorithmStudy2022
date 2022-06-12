n, k = map(int, input().split())

count = 0
coinlist = []

for _ in range(n):
    coinlist.append(int(input()))

coinlist.sort(reverse=True)

for coin in coinlist:
    count += k//coin
    k %= coin

print(count)