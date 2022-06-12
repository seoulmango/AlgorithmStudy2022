pastas = []
juices = []

for _ in range(3):
    pasta = int(input())
    pastas.append(pasta)

for _ in range(2):
    juice = int(input())
    juices.append(juice)

ans = min(pastas)*1.1 + min(juices)*1.1
ans = round(ans, 1)
print(ans)