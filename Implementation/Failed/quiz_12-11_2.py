from collections import deque

n = int(input())
k = int(input())

klist= []
for _ in range(k):
    klist.append(list(map(int, input().split())))

l = int(input())

llist = []
for _ in range(l):
    llist.append(list(input().split()))

new_llist = []
for i in range(1, len(llist)):
    new_llist.append([int(llist[i][0]) - int(llist[i-1][0]), llist[i][1]])
llist = new_llist

def walk(location, head, turn):
    x = location[0]
    y = location[1]
    if head == 'E':
        if turn == 'L':
            x -= 1
            head = 'N'
        else:
            x += 1
            head = 'S'
    elif head == 'W':
        if turn == 'L':
            x += 1
            head = 'S'
        else:
            x -= 1
            head = 'N'
    elif head == 'N':
        if turn == 'L':
            y -= 1
            head = 'W'
        else:
            y += 1
            head = 'E'
    elif head == 'S':
        if turn == 'L':
            y += 1
            head = 'E'
        else:
            y -= 1
            head = 'W'

    return [x,y], head

x, y = 1, 1
snake = deque([[1, 1]])
# 머리 방향
snakehead = 'E'
time = 0
gameover = False

for move in llist:
    for _ in range(int(move[0])):
        new_step, new_head = walk(snake[-1], snakehead, move[1])
        if new_step in klist:
            snake.append(new_step)
            time += 1
        elif new_step in snake:
            gameover = True
            time += 1
            break
        elif new_step[0] not in range(1, n+1) or new_step[1] not in range(1, n+1):
            gameover = True
            time += 1
            break
        else:
            snake.append(new_step)
            snake.popleft()
            time += 1
        print(snake)
    snakehead = new_head

    if gameover:
        break

print(time)