from operator import contains
import itertools

n = int(input())

coins = list(map(int, input().split()))

coins.sort()

# coins의 조합으로 구할 수 있는 모든 수 리스트에 저장하기
possible_sum = []
for i in range(1, n+1):
    nCr = itertools.combinations(coins, i)
    for combination in nCr:
        possible_sum.append(sum(combination))
    possible_sum = list(set(possible_sum))

# 중복 없이 순서대로 정렬
possible_sum.sort()

# 1부터 셌을 때, 가능한 합에서 그 숫자가 없을 경우
# 그 수를 print한다.
i = 0
for sum in possible_sum:
    i += 1
    if i != sum:
        print(i)
        break
