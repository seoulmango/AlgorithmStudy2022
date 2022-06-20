from collections import deque

n, m = map(int, input().split())

maze = []

for _ in range(n):
    maze.append(list(map(int, input())))

def bfs(x, y, maze):
    queue = deque()
    queue.append((x,y))

    dx = [1, -1 ,0, 0]
    dy = [0, 0 , 1, -1]

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[-1][-1]

print(bfs(0,0, maze))
print(maze)