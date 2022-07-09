def solution(w, h, board):
    count = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j,board) == True:
                count += 1
    return count

def dfs(x, y, board):
    if x < 0 or y < 0 or x >= h or y >= w:
        return False
    if board[x][y] == 1:
        board[x][y] = 2
        dfs(x-1, y-1, board)
        dfs(x-1, y, board)
        dfs(x-1, y+1, board)
        dfs(x, y+1, board)
        dfs(x, y-1, board)
        dfs(x+1, y-1, board)
        dfs(x+1, y, board)
        dfs(x+1, y+1, board)
        return True
    return False



while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    board = []
    for _ in range(h):
        board.append(list(map(int, input().split())))

    print(solution(w,h,board))