n = int(input())

n = 1000-n

coinlist = [500, 100, 50, 10, 5, 1]
count = 0

for coin in coinlist:
    count += n//coin
    n %= coin

print(count)