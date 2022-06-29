n = int(input())
nlist = []
for _ in range(n):
    nlist.append(int(input()))
nlist = sorted(nlist, reverse=True)

for i in nlist:
    print(i, end=" ")