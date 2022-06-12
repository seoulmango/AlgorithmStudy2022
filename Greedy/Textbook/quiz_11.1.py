# 총 모험자 수 받기 (사실 필요 없음)
n = int(input())

# 모험자를 리스트 안에 넣기
travelers = list(map(int, input().split()))

# 공포도 순으로 정렬
travelers.sort()

# 여행을 떠날 수 있는 그룹들
groups = []

# 여행을 떠날 수 있는 각각의 그룹
# ex) groups = [[new_group1], [new_group2], [new_group3]]
new_group = []

# 공포도가 가장 낮은 여행자부터 new_group리스트에 넣는다.
# new_group 리스트 안에 있는 "가장 공포도가 큰 여행자의 공포도" <= "new_group 여행자의 수"라면
# new_group을 groups에 append한다.
for traveler in travelers:
    new_group.append(traveler)
    if len(new_group) >= max(new_group):
        groups.append(new_group)
        new_group = []

print(len(groups))