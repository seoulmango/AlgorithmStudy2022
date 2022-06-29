n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input())))

def fillout(x, y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    elif board[x][y] == 0:
        board[x][y] = 1
        fillout(x+1, y)
        fillout(x-1, y)
        fillout(x, y+1)
        fillout(x, y-1)
        return True
    return False

ans = 0
for i in range(n):
    for j in range(m):
        if fillout(i, j) == True:
            ans += 1

print(ans)