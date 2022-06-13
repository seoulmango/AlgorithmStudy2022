n, m = map(int, input().split())

x, y, d = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[x, y]]
turns = 0

while True:
    # 같은 자리에서 4번 돌았을 경우
    if turns == 4:
        if d == 0:
        # 왼쪽의 인덱스값
            nx = x+1
            ny = y
            # 지도 안에 있고, 육지이고, 방문하지 않았을 때
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == 0:
                x = nx
                y = ny
                d = 3
                if [nx, ny] not in visited:
                    visited.append([nx, ny])
                turns = 0
            # 왼쪽으로 못 갈 경우 방향만 돌린다.
            else:
                break
        elif d == 1:
            nx = x
            ny = y-1
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == 0:
                x = nx
                y = ny
                d = 0
                if [nx, ny] not in visited:
                    visited.append([nx, ny])
                turns = 0
            else:
                break
        elif d == 2:
            nx = x-1
            ny = y
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == 0:
                x = nx
                y = ny
                d = 1
                if [nx, ny] not in visited:
                    visited.append([nx, ny])
                turns = 0
            else:
                break
        elif d == 3:
            nx = x
            ny = y+1
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == 0:
                x = nx
                y = ny
                d = 2
                if [nx, ny] not in visited:
                    visited.append([nx, ny])
                turns = 0
            else:
                break

    # 왼쪽에 위치한 지형 확인하기
    if d == 0:
        # 왼쪽의 인덱스값
        nx = x
        ny = y-1
        # 지도 안에 있고, 육지이고, 방문하지 않았을 때
        if 0<=nx<n and 0<=ny<m and board[nx][ny] == 0 and [nx, ny] not in visited:
            x = nx
            y = ny
            d = 3
            visited.append([nx, ny])
            turns = 0
        # 왼쪽으로 못 갈 경우 방향만 돌린다.
        else:
            turns += 1
            d = 3
    elif d == 1:
        nx = x-1
        ny = y
        if 0<=nx<n and 0<=ny<m and board[nx][ny] == 0 and [nx, ny] not in visited:
            x = nx
            y = ny
            d = 0
            visited.append([nx, ny])
            turns = 0
        else:
            turns += 1
            d = 0
    elif d == 2:
        nx = x
        ny = y+1
        if 0<=nx<n and 0<=ny<m and board[nx][ny] == 0 and [nx, ny] not in visited:
            x = nx
            y = ny
            d = 1
            visited.append([nx, ny])
            turns = 0
        else:
            turns += 1
            d = 1
    elif d == 3:
        nx = x+1
        ny = y
        if 0<=nx<n and 0<=ny<m and board[nx][ny] == 0 and [nx, ny] not in visited:
            x = nx
            y = ny
            d = 2
            visited.append([nx, ny])
            turns = 0
        else:
            turns += 1
            d = 2

print(len(visited))

print(visited)