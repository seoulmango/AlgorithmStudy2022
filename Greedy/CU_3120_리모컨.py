# 리모컨

# 1, 5, 10도 이동 하고 나서의 값과 도달해야 하는 값의 차이가 가장 적은 것을 선택

a, b = map(int, input().split())
count = 0

while True:
    if a < b:
        add10 = b - (a + 10)
        add5 = b - (a + 5)
        add1 = b - (a + 1)
        distance = min(abs(add10), abs(add5), abs(add1))
        a = b - distance
        count += 1
        if a == b:
            break
    elif a > b:
        min10 = b - (a - 10)
        min5 = b - (a - 5)
        min1 = b - (a - 1)
        distance = min(abs(min10), abs(min5), abs(min1))
        a = b - distance
        count += 1
        if a == b:
            break
    else:
        break

print(count)