# 열쇠 돌리기
def rotate(array):
    row, col = len(array), len(array[0])
    newArr = [[None]*row for _ in range(col)]
    for c in range(col):
        for r in range(row):
            newArr[c][row-r-1] = array[r][c]
    return newArr

# 비교하기
def compare(key, newlock):
    answer = False
    m = len(key)
    n = len(newlock) - 2*m

    for i in range(m+n+1):
        for j in range(m+n+1):
            for x in range(m):
                for y in range(m):
                    newlock[i+x][j+y] += key[x][y]     
            if check(key, newlock) is True:
                return True
            for x in range(m):
                for y in range(m):
                    newlock[i+x][j+y] -= key[x][y]
    return answer

# 가운데 부분 확인하기
def check(key, newlock):
    m = len(key)
    n = len(newlock) - 2*m
    for i in range(m, n+m):
        for j in range(m, n+m):
            if newlock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)

    # 비교할 자물쇠 만들기
    newlock = [[0] * (2*m + n)] * m
    for i in range(n):
        newlock.append([0]*m + lock[i] + [0]*m)
    newlock += [[0] * (2*m + n)] * m

    # 돌려가며 반복
    for _ in range(4):
        key = rotate(key)
        if compare(key, newlock) is True:
            return True
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))