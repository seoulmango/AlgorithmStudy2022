n = int(input())

stlist = []
for _ in range(n):
    input_data = input().split()
    stlist.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))

# 국어 성적 내림차순, 영어 오름차순, 수학 내림차순, 이름 오름차순
stlist.sort(key = lambda student: (-student[1], student[2], -student[3], student[0]))
for st in stlist:
    print(st[0])