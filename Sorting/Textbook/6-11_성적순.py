n = int(input())
stlist = []
for _ in range(n):
    name, score = input().split()
    stlist.append((int(score), name))

stlist.sort(key=lambda student: student[0])

for st in stlist:
    print(st[1], end=" ")