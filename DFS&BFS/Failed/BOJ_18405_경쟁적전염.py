n, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
s, X, Y = map(int, input().split())

X, Y = X-1, Y-1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def virus(x,y):
    nlist = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        elif board[nx][ny] == 0:
            nlist.append((nx, ny))
    return nlist

for _ in range(s):
    vlist = [[] for _ in range(k+1)]

    # 바이러스 1번부터 순서대로 확산
    for v in range(1, k+1):
        for i in range(n):
            for j in range(n):
                if board[i][j] == v:
                    vlist[v].append(virus(i,j))
    
    # 높은 수의 바이러스는 낮은 수의 바이러스로 갈아치울 수 있다
    for vtype in range(len(vlist)-1, 0, -1):
        for vspread in vlist[vtype]:
            for (x,y) in vspread:
                board[x][y] = vtype

for row in board:
    print(row)
print(board[X][Y])