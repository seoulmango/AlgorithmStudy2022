n = int(input())

count = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            # 시분초에 3이 포함돼 있다면 세기
            if '3' in str(h) + str(m) + str(s):
                count += 1

print(count)