def rotate_anticlockwise(array):
    row, col = len(array), len(array[0])
    # 열과 행의 수가 뒤바뀌게 새로 만들기
    newArr = [[None]*row for _ in range(col)]
    for c in range(col):
        for r in range(row-1, -1, -1):
            newArr[col-c-1][r] = array[r][c]
    return newArr

'''
1  2  3  4  5
6  7  8  9  10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

위에서 아래로 바꾸기
각 col의 마지막을 row로 시작한다.

5  10 15 20 25
4  9  14 19 24
3  8  13 18 23
2  7  12 17 22
1  6  11 16 21
'''

def rotate_clockwise(array):
    row, col = len(array), len(array[0])
    newArr = [[None]*row for _ in range(col)]
    for c in range(col):
        for r in range(row):
            newArr[c][row-r-1] = array[r][c]
    return newArr

'''
1  2  3  4  5
6  7  8  9  10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

21 16 11  6  1  
22 17 12  7  2
23 18 13  8  3
24 19 14  9  4
25 20 15 10  5
'''

def rotate_anticlockwise(array):
    return list(zip(*array[::-1]))