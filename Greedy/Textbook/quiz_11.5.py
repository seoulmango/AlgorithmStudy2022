import itertools
n, k = map(int, input().split())

balls = list(map(int, input().split()))

# 서로 다른 무게의 가짓수
comb_weight = []
balls_weight = list(set(balls))
for combination in itertools.combinations(balls_weight, 2):
    comb_weight.append(combination)

# 각 무게의 공의 개수만큼 곱한다
ans = 0
for combination in comb_weight:
    ans += balls.count(combination[0]) * balls.count(combination[1])

print(ans)