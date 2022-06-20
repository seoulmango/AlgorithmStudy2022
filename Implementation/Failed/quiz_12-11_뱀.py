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

x, y = 1, 1
snake = deque([[1, 1]])
direction = 4
time = 0
gameover = False

for location in llist:

    # 오른쪽 방향
    if direction == 4:
        if location[1]=='L':
            for _ in range(int(location[0])):
                x -= 1
                time += 1
                if x > n or x < 1:
                    gameover = True
                    break
                elif [x, y] in klist:
                    snake.append([x,y])
                elif [x, y] in snake:
                    gameover = True
                    break
                else:
                    snake.append([x,y])
                    snake.popleft()
            direction = 1
        elif location[1]=='D':
            for _ in range(int(location[0])):
                x += 1
                time += 1
                if x > n or x < 1:
                    gameover = True
                    break
                elif [x, y] in klist:
                    snake.append([x,y])
                elif [x, y] in snake:
                    gameover = True
                    break
                else:
                    snake.append([x,y])
                    snake.popleft()
            
            direction = 2

    # 위 방향
    elif direction == 1:
        if location[1]=='L':
            for _ in range(int(location[0])):
                y -= 1
                time += 1
                if y > n or y < 1:
                    gameover = True
                    break
                elif [x, y] in klist:
                    snake.append([x,y])
                elif [x, y] in snake:
                    gameover = True
                    break
                else:
                    snake.append([x,y])
                    snake.popleft()
            direction = 3
        elif location[1]=='D':
            for _ in range(int(location[0])):
                y += 1
                time += 1
                if y > n or y < 1:
                    gameover = True
                    break
                elif [x, y] in klist:
                    snake.append([x,y])
                elif [x, y] in snake:
                    gameover = True
                    break
                else:
                    snake.append([x,y])
                    snake.popleft()
            direction = 4

    # 아래 방향
    elif direction == 2:
        if location[1]=='L':
            for _ in range(int(location[0])):
                y += 1
                time += 1
                if y > n or y < 1:
                    gameover = True
                    break
                elif [x, y] in klist:
                    snake.append([x,y])
                elif [x, y] in snake:
                    gameover = True
                    break
                else:
                    snake.append([x,y])
                    snake.popleft()
            direction = 4
        elif location[1]=='D':
            for _ in range(int(location[0])):
                y -= 1
                time += 1
                if y > n or y < 1:
                    gameover = True
                    break
                elif [x, y] in klist:
                    snake.append([x,y])
                elif [x, y] in snake:
                    gameover = True
                    break
                else:
                    snake.append([x,y])
                    snake.popleft()
            direction = 3

    # 왼쪽 방향
    elif direction == 3:
        if location[1]=='L':
            for _ in range(int(location[0])):
                x += 1
                time += 1
                if x > n or x < 1:
                    gameover = True
                    break
                elif [x, y] in klist:
                    snake.append([x,y])
                elif [x, y] in snake:
                    gameover = True
                    break
                else:
                    snake.append([x,y])
                    snake.popleft()
            direction = 2
        elif location[1]=='D':
            for _ in range(int(location[0])):
                x -= 1
                time += 1
                if x > n or x < 1:
                    gameover = True
                    break
                elif [x, y] in klist:
                    snake.append([x,y])
                elif [x, y] in snake:
                    gameover = True
                    break
                else:
                    snake.append([x,y])
                    snake.popleft()
            direction = 1

    if gameover:
        break

print(time)