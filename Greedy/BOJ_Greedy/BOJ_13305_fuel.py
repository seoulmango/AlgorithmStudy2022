# 다음 도시로 이동 할 때마다 가장 싼 값을 갱신

n = int(input())

# 각 도시간의 거리
dist = list(map(int, input().split()))

# 각 도시의 기름 가격
fuel = list(map(int, input().split()))

cheap = fuel[0]
cost = 0

for i in range(n-1):
    if fuel[i] < cheap:
        cheap = fuel[i]
    cost += cheap * dist[i]

print(cost)