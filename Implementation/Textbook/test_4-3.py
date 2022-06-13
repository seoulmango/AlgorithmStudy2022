place = input()
x = place[0]
y = int(place[1])

rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# 열 위치를 숫자로 바꾸기
for i in range(len(rows)):
    if rows[i] == x:
        x = i+1
        break

dx = [2, 2, -2, -2, 1, 1, -1 , -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]
count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<nx<9  and 0<ny<9 :
        count += 1

print(count)