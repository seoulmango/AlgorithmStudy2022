from itertools import combinations
import copy

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 빈 공간 리스트
empty = []
# 바이러스 공간 리스트
virus = []
for x in range(n):
    for y in range(m):
        if board[x][y] == 0:
            empty.append((x,y))
        elif board[x][y] == 2:
            virus.append((x,y))

# 빈 공간들 중 3군데를 고르는 모든 경우의 수 (벽으로 설치할 것)
wall = list(combinations(empty, 3))


def dfs(v, board):
    x = v[0]
    y = v[1]
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    # 빈 공간이라면 바이러스로 전염시킨다.
    if board[x][y] == 0:
        board[x][y] = 2
        # 재귀함수
        dfs((x+1, y), board)
        dfs((x-1, y), board)
        dfs((x, y+1), board)
        dfs((x, y-1), board)


ans = -1

# 벽을 설치할 수 있는 모든 경우의 수에 대하여
for trial in wall:
    space = 0
    # 처음에 주어진 보드를 deepcopy하여 변경사항이 없도록 한다.
    board2 = copy.deepcopy(board)

    # 벽 좌표에 벽을 세운다 (0을 1로 변경)
    for w in trial:
        board2[w[0]][w[1]] = 1
    # 바이러스 좌표를 0으로 변경한다. (그래야만 dfs 함수가 작동한다.)
    for v in virus:
        board2[v[0]][v[1]] = 0
    # 각 바이러스 좌표 별로 함수를 작동한다.
    for v in virus:
        dfs(v, board2)
    # 전염 이후, 보드 위의 0의 숫자를 센다
    for r in board2:
        space += r.count(0)
    if space > ans:
        ans = space

print(ans)