import copy

r, c, t = map(int, input().split())
room = []
for _ in range(r):
    room.append(list(map(int, input().split())))

cleaner = []
for i in range(r):
    if room[i][0] == -1:
        cleaner.append((i, 0))

# 확산시키는 함수
def diffuse(room):
    # 새 방 좌표 만들기
    newroom = copy.deepcopy(room)

    # 해당 좌표의 상하좌우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    # 방의 모든 칸에 대하여
    for x in range(len(room)):
        for y in range(len(room[0])):
            # 공기청정기 자리면 건너뛰기
            if room[x][y] == -1:
                continue

            # 확산된 횟수
            di = 0

            # 상하좌우 전부 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 범위 안에서만
                if -1 < nx < len(room) and -1 < ny < len(room[0]):
                    # 공기청정기가 없는 칸이라면 확산
                    if newroom[nx][ny] != -1:
                        newroom[nx][ny] += room[x][y]//5
                        di += 1

            # 확산 횟수만큼 값 빼주기
            newroom[x][y] -= (room[x][y]//5) * di

    return newroom

# 미세먼지 공기청정기로 이동
def wind(room, cleaner):
    newroom = copy.deepcopy(room)

    R = len(newroom)
    C = len(newroom[0])

    # 공기 청정기 좌표
    x1 = cleaner[0][0]
    x2 = cleaner[1][0]

    # 공기 청정기 바로 오른쪽은 0
    newroom[x1][1] = 0
    newroom[x2][1] = 0

    # 오른쪽으로 이동하는 줄
    for i in range(1, C-1):
        newroom[x1][i + 1] = room[x1][i]
        newroom[x2][i + 1] = room[x2][i]

    # 상체 위 이동
    for i in range(x1-1, -1, -1):
        newroom[i][-1] = room[i+1][-1]
    

    # 상체 왼쪽 이동
    for i in range(C-2, -1, -1):
        newroom[0][i] = room[0][i+1]
    
    # 상체 아래 이동
    for i in range(1, x1):
        newroom[i][0] = room[i-1][0]

    # 하체 아래 이동
    for i in range(1, R-x2):
        newroom[x2 + i][C-1] = room[x2 + i -1][C-1]

    # 하체 왼쪽 이동
    for i in range(C-2, -1, -1):
        newroom[R-1][i] = room[R-1][i+1]

    # 하체 위에 이동
    for i in range(R-2, x2, -1):
        newroom[i][0] = room[i+1][0]

    return newroom

# 주어진 시간 동안 작동시킨다
for _ in range(t):
    room = diffuse(room)
    room = wind(room, cleaner)

# 공기청정기 개수만큼 더하고 (+2)
# 방에 있는 미세먼지의 합을 구한다.
ans = 2
for row in room:
    ans += sum(row)

print(ans)