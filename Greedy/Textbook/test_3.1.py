n = int(input())

coinlist = [500, 100, 50, 10]
count = 0

for coin in coinlist:
    count += n//coin
    n %= coin

print(coin)