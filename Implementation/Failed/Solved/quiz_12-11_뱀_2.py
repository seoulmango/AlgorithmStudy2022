from collections import deque

n = int(input())
k = int(input())
# 보드판 만들기
board = [[0 for _ in range(n)] for _ in range(n)]

# 사과 위치 리스트
apples = []
for _ in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    apples.append([x,y])

l = int(input())

# 뱀 움직임 리스트
moves = []
for _ in range(l):
    x, c = input().split()
    x = int(x)
    moves.append([x, c])

# 좌측 상단에 뱀 위치
snake = deque()
snake.append([0,0])

# 보드에 사과 놓기
for apple in apples:
    board[apple[0]][apple[1]] = 1

# 처음에 동쪽을 향함
head = 'E'

# 한 칸 움직이는 함수
def crawl(head, x, y):
    if head == 'N':
        x -=1
    elif head == 'S':
        x += 1
    elif head == 'E':
        y += 1
    elif head == 'W':
        y -= 1
    return x, y

# 머리 돌리는 함수
def turn(c, head):
    if c == 'L':
        if head == 'N':
            head = 'W'
        elif head == 'S':
            head = 'E'
        elif head == 'E':
            head = 'N'
        elif head == 'W':
            head = 'S'
    elif c == 'D':
        if head == 'N':
            head = 'E'
        elif head == 'S':
            head = 'W'
        elif head == 'E':
            head = 'S'
        elif head == 'W':
            head = 'N'
    return head

time = 0
t = moves[0][0]
gameover = False
for i in range(len(moves)):
    if i == 0:
        t = moves[i][0]
    else:
        t = moves[i][0] - moves[i-1][0]
    c = moves[i][1]
    # 해당 시간만큼 이동하기
    for _ in range(t):
        nx, ny = crawl(head, snake[-1][0], snake[-1][1])
        time += 1

        # 보드를 넘어갔을 때
        if nx >= len(board) or ny >= len(board) or nx < 0 or ny < 0:
            gameover = True
        # 몸으로 이동했을 때
        elif [nx, ny] in snake:
            gameover = True
        # 빈 공간일 때
        elif board[nx][ny] == 0:
            snake.append([nx, ny])
            snake.popleft()
        # 사과를 먹었을 때
        elif board[nx][ny] == 1:
            board[nx][ny] = 0
            snake.append([nx, ny])
        # 게임 오버일 때 탈출
        if gameover:
            break

    # 게임 오버일 때 탈출
    if gameover:
        break

    # 머리 돌리기
    head = turn(c, head)

# 게임오버 아니면, 벗어날 때까지 계속 움직이기
while not gameover:
    nx, ny = crawl(head, snake[-1][0], snake[-1][1])
    time += 1

    # 보드를 넘어갔을 때
    if nx >= len(board) or ny >= len(board) or nx < 0 or ny < 0:
        gameover = True
    # 몸으로 이동했을 때
    elif [nx, ny] in snake:
        gameover = True
    # 빈 공간일 때
    elif board[nx][ny] == 0:
        snake.append([nx, ny])
        snake.popleft()
    # 사과를 먹었을 때
    elif board[nx][ny] == 1:
        board[nx][ny] = 0
        snake.append([nx, ny])
    
    if gameover:
        break

print(time)