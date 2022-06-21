n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append((list(map(int, input().split()))))

# 벽 개수
walls = 0
for row in board:
    walls += row.count(6)

# 카메라 종류 & 위치 저장
camera = []
for r in range(n):
    for c in range(m):
        if board[r][c] != 6 and board[r][c] != 0:
            camera.append([board[r][c], r, c])

# 동서남북 중 하나로 볼 때 가시 범위
def vision(board, dir, x, y):
    visionlist = []
    if dir == 'N':
        while True:
            x -= 1
            # 보드 벗어나면 break
            if x < 0 or x >= len(board):
                break
            else:
                item = board[x][y]
                # 벽을 만날 때
                if item == 6:
                    break
                # 카메라를 만날 때
                elif item in [1, 2, 3, 4, 5]:
                    continue
                # 빈 공간일 때
                else:
                    visionlist.append((x,y))
    if dir == 'S':
        while True:
            x += 1
            # 보드 벗어나면 break
            if x < 0 or x >= len(board):
                break
            else:
                item = board[x][y]
                # 벽을 만날 때
                if item == 6:
                    break
                # 카메라를 만날 때
                elif item in [1, 2, 3, 4, 5]:
                    continue
                # 빈 공간일 때
                else:
                    visionlist.append((x,y))
    if dir == 'E':
        while True:
            y += 1
            # 보드 벗어나면 break
            if y < 0 or y >= len(board[0]):
                break
            else:
                item = board[x][y]
                # 벽을 만날 때
                if item == 6:
                    break
                # 카메라를 만날 때
                elif item in [1, 2, 3, 4, 5]:
                    continue
                # 빈 공간일 때
                else:
                    visionlist.append((x,y))
    if dir == 'W':
        while True:
            y -= 1
            # 보드 벗어나면 break
            if y < 0 or y >= len(board[0]):
                break
            else:
                item = board[x][y]
                # 벽을 만날 때
                if item == 6:
                    break
                # 카메라를 만날 때
                elif item in [1, 2, 3, 4, 5]:
                    continue
                # 빈 공간일 때
                else:
                    visionlist.append((x,y))
    return visionlist

# 카메라에 따라 가능한 방향 조합
def directions(cameratype):
    if cameratype == 1:
        return [['N'], ['S'], ['E'], ['W']]
    elif cameratype == 2:
        return [['E', 'W'], ['N', 'S']]
    elif cameratype == 3:
        return [['N', 'E'], ['E', 'S'], ['S', 'W'], ['W', 'N']]
    elif cameratype == 4:
        return [['S', 'E', 'W'], ['N', 'E', 'W'], ['N', 'S', 'W'], ['N', 'S', 'E']]
    elif cameratype == 5:
        return [['N', 'S', 'E', 'W']]

# 카메라 최대 8대
visionlists = []
for _ in range(8):
    visionlists.append([])

# 각각의 카메라에 대하여
for cam_idx in range(len(camera)):
    # 카메라 정보
    cameratype = camera[cam_idx][0]
    x = camera[cam_idx][1]
    y = camera[cam_idx][2]
    # 카메라가 바라볼 수 있는 방향 조합
    for directions_possible in directions(cameratype):
        l = []
        # 조합 가능한 방향을 동시에 바라볼 때의 시야 합치기
        for d in directions_possible:
            l += vision(board, d, x, y)
        visionlists[cam_idx].append(l)
    

# 카메라 별로 볼 수 가시 범위의 조합은 전부 구해놓음
# 이걸 어케 계산한담...

for cam in visionlists:
    cam += [[]]

ans = n*m

comparelist = []
for a in range(len(visionlists[0])):
    comparelist_a = visionlists[0][a]
    for b in range(len(visionlists[1])):
        comparelist_b = comparelist_a + visionlists[1][b]
        for c in range(len(visionlists[2])):
            comparelist_c = comparelist_b + visionlists[2][c]
            for d in range(len(visionlists[3])):
                comparelist_d = comparelist_c + visionlists[3][d]
                for e in range(len(visionlists[4])):
                    comparelist_e = comparelist_d + visionlists[4][e]
                    for f in range(len(visionlists[5])):
                        comparelist_f = comparelist_e + visionlists[5][f]
                        for g in range(len(visionlists[6])):
                            comparelist_g = comparelist_f + visionlists[6][g]
                            for h in range(len(visionlists[7])):
                                comparelist_h = comparelist_g + visionlists[7][h]
                                # 중복 제거
                                set_comparelist = set(comparelist_h)
                                # 정답 갱신
                                ans = min(ans, n*m - len(set_comparelist) - walls - len(camera))

print(ans)