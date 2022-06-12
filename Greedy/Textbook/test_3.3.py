# 행과 열 값 받기
N, M = map(int, input().split())

# 카드의 나열 리스트
cards = []

# 각 행 당 가장 작은 수
smallest = []

# 카드 리스트 만들기
for i in range(N):
    row = list(map(int, input().split()))
    cards.append(row)

# 행 당 가장 작은 수 찾기
for row in cards:
    pick = min(row)
    smallest.append(pick)

print(max(smallest))