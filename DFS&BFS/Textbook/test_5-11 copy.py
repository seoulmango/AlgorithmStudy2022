from collections import deque

n, m = map(int, input().split())

maze = []

for _ in range(n):
    maze.append(list(map(int, input())))

exit_x, exit_y = n-1, m-1

visited = [[False for _ in range(m)] for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(maze):
    start = (0, 0)
    queue = deque([start])
    while len(queue) >= 1:
        v = queue.popleft()
        for i in range(4):
            if v[0]+dx[i] < 0 or v[0]+dx[i] >= n or v[1]+dy[i] < 0 or v[1]+dy[i] >= m:
                pass
            elif maze[v[0]+dx[i]][v[1]+dy[i]] == 1:
                maze[v[0]+dx[i]][v[1]+dy[i]] += maze[v[0]][v[1]]
                queue.append((v[0]+dx[i], v[1]+dy[i]))

    return maze[-1][-1]

print(bfs(maze))