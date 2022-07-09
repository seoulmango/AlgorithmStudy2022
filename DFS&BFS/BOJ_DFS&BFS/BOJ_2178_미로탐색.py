import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

maze = []

for _ in range(n):
    maze.append(list(map(int, sys.stdin.readline().rstrip())))

queue = deque([(0,0)])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(maze, queue):
    while queue:
        v = queue.popleft()
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            elif maze[nx][ny] == 1:
                maze[nx][ny] += maze[v[0]][v[1]]
                queue.append((nx,ny))
    return maze[-1][-1]

print(bfs(maze, queue))