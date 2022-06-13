# 상하좌우

# 지도 크기 받기
n = int(input())

# 이동 계획 받아서 리스트에 저장
plan = list(input().split())

location = [1,1]
for move in plan:
    if move == "U":
        if location[0] == 1:
            continue
        else:
            location[0] -= 1
    elif move == "D":
        if location[0] == n:
            continue
        else:
            location[0] += 1
    elif move == "L":
        if location[1] == 1:
            continue
        else:
            location[1] -= 1
    elif move == "R":
        if location[1] == n:
            continue
        else:
            location[1] += 1

print(location[0], location[1])