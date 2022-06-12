n, k = map(int, input().split())
count = 0

while True:
    divisor = (n//k)*k
    # 나눌 수 있을 때까지 1 빼기
    count += n - divisor
    n = divisor

    if n >= k:
        n //= k
        count += 1
    
    if n < k or n == 1:
        break

if n != 1:
    count += (n-1)

print(count)