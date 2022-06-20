def rotation(key):
    new_key = [[[None] for _ in range(len(key))] for _ in range(len(key))]
    for x in range(len(key)):
        for y in range(len(key)-1, -1, -1):
            new_key[len(key)-x-1][y] = key[y][x]
    key = new_key 
    return key


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