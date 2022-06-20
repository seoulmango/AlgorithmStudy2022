from itertools import combinations

n, m = map(int, input().split())

town = []
for _ in range(n):
    town.append(list(map(int, input().split())))


homes = []
stores = []
dist = []

for row in range(n):
    for col in range(n):
        if town[row][col] == 1:
            homes.append([row, col])
        elif town[row][col] == 2:
            stores.append([row, col])

store_choices = list(combinations(stores, m))

answer = 999999999999999999999

for choice in store_choices:
    town_distance = 0
    for home_idx in range(len(homes)):
        min_dist = None
        for store in choice:
            distance = abs(homes[home_idx][0] - store[0]) + abs(homes[home_idx][1] - store[1])
            if min_dist == None or min_dist > distance:
                min_dist = distance
        town_distance += min_dist
    if town_distance < answer:
        answer = town_distance

print(answer)