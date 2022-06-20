n, m = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(int, input())))

print(board)

def dfs(x,y):
    # 범위 벗어날 때
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 방문하지 않은 노드일 때
    if board[x][y] == 0:
        board[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

ans = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            ans += 1

print(ans)