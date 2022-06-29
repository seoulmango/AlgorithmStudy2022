# (x, y)를 시계방향으로 90도 회전 시: (y, -x)가 된다.
# 반시계방향은 (-y, x)

n = int(input())

dcurves = []
allpoints = [[] for _ in range(n)]
center = []
for _ in range(n):
    x, y, d, g = map(int, input().split())
    dcurves.append((x, y, d, g))

def drawline(x, y, d):
    if d == 0:
        x += 1
    elif d == 1:
        y += 1
    elif d == 2:
        x -= 1
    elif d ==3:
        y -=1
    return x, y

def turn90(cx, cy, points):
    newpoints = []
    for point in points:
        newpoints.append((point[1] - cy + cx, cx-point[0] + cy))
    points += newpoints
    cx, cy = newpoints[0][0], newpoints[0][1]
    return cx, cy, points

for i in range(n):
    x = dcurves[i][0]
    y = dcurves[i][1]
    d = dcurves[i][2]
    g = dcurves[i][3]

    allpoints[i].append((x,y))
    nx, ny = drawline(x, y, d)
    allpoints[i].append((nx, ny))
    center.append((nx,ny))
    print('센터:', center)
    for _ in range(g):
        cx, cy, newpoints = turn90(center[i][0], center[i][1], allpoints[i])
        center[i] = (cx, cy)
        allpoints[i] = newpoints

answer_set = []
for curve in allpoints:
    answer_set += curve

count = 0
for x in range(101):
    for y in range(101):
        if (x, y) in answer_set:
            if (x+1, y) in answer_set:
                if (x, y+1) in answer_set:
                    if (x+1, y+1) in answer_set:
                        count += 1
print(count)