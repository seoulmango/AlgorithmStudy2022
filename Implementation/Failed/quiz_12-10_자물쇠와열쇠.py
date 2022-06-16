def rotation(key):
    # key를 정반대 값으로 바꾸기
    for x in range(len(key)):
        for y in range(len(key)):
            if key[x][y] == 0:
                key[x][y] == 1
            else:
                key[x][y] == 0

    # 열쇠를 회전한 모든 값
    four_keys = [[key]]

    while len(four_keys)<4:
        new_key = [[None]*len(key) for _ in range(len(key))]
        for x in range(len(key)):
            for y in range(len(key)-1, -1, -1):
                new_key[len(key)-x-1][y] = key[y][x]
        four_keys.append(new_key)
        key = new_key
    
    return four_keys


def solution(key, lock):
    answer = False

    # 열쇠가 움직일 수 있는 보드 만들기
    testboard = [['x']*(len(lock)+len(key)*2-2) for _ in range(len(key)-1)]
    for line in lock:
        testboard.append(['x']*(len(key)-1)+line+['x']*(len(key)-1))
    for _ in range(len(key)-1):
        testboard.append(['x']*(len(lock)+len(key)*2-2))
    

    for key in rotation(key):
        # 가로로 한 칸씩 이동하며 모든 층 비교
        comparison = []
        for i in range(len(lock) + len(key) - 2):
            for h in range(len(lock) + len(key) - 2):
                for l in range(len(key)):
                    comparison.append(testboard[h+l][i:i+len(key)])
                
                # comparison과 key 비교하기
                for x in range(len(key)):
                    for y in range(len(key)):
                        if comparison[x][y] == 'x':
                            pass
                        elif comparison[x][y] == key[x][y]:
                            answer = True
                        elif comparison[x][y] != key[x][y]:
                            answer = False
                            break
                if answer is True:
                    break
                else:
                    comparison = []
    return answer