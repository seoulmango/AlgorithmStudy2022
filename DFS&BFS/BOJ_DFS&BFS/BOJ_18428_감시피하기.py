import sys
from itertools import combinations

n = int(sys.stdin.readline().rstrip())
board = []
tlist = []
slist = []
xlist = []

for i in range(n):
    board.append(list(sys.stdin.readline().rstrip().split()))
    for j in range(n):
        a = board[i][j]
        if a == 'X':
            xlist.append((i,j))
        elif a == 'S':
            slist.append((i,j))
        else:
            tlist.append((i,j))

olist = combinations(xlist, 3)

def check(tlist, slist, olist, board, n):
    visual = []
    for t in tlist:
        x = t[0]
        y = t[1]
        
        # 왼쪽
        nx = x + 1 - 1
        ny = y + 1 - 1
        while True:
            ny -= 1
            if ny < 0 or ny >= n or (nx, ny) in olist:
                break
            visual.append((nx, ny))

        # 오른쪽
        nx = x + 1 - 1
        ny = y + 1 - 1
        while True:
            ny += 1
            if ny < 0 or ny >= n or (nx, ny) in olist:
                break
            visual.append((nx, ny))

        # 위
        nx = x + 1 - 1
        ny = y + 1 - 1
        while True:
            nx -= 1
            if nx < 0 or nx >= n or (nx, ny) in olist:
                break
            visual.append((nx, ny))

        # 아래
        nx = x + 1 - 1
        ny = y + 1 - 1
        while True:
            nx += 1
            if nx < 0 or nx >= n or (nx, ny) in olist:
                break
            visual.append((nx, ny))

    for s in slist:
        if s in visual:
            return False
    return True

for trial in olist:
    if check(tlist, slist, trial, board, n) == True:
        print('YES')
        break
else:
    print('NO')
