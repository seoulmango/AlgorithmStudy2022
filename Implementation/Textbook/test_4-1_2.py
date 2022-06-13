n = int(input())

x, y = 1, 1

plans = list(input().split())

move = ['L', 'R', 'U', 'D']
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

for plan in plans:
    for i in range(len(move)):
        if plan == move[i]:
            next_x = x + dx[i]
            next_y = y + dy[i]
            break
    if next_x < 1 or next_y < 1:
        continue
    else:
        x = next_x
        y = next_y

print(y, x)