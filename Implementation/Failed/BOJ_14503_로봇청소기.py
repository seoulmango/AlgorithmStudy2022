n, m = map(int, input().split())

r, c, d = map(int, input().split())

room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

def go_left(r, c, d):
    if d == 0:
        d = 3
        c -= 1

    elif d == 1:
        d = 0
        r -= 1

    elif d == 2:
        d = 1
        c += 1

    elif d == 3:
        d = 2
        r += 1
    
    return(r, c, d)

def go_back(r, c, d):
    if d == 0:
        r += 1

    elif d == 1:
        c -= 1

    elif d == 2:
        r -= 1

    elif d == 3:
        c += 1
    
    return(r, c, d)

cleaned = [[r, c]]
turns = 0
while True:
    new_r, new_c, new_d = go_left(r, c, d)
    turns += 1
    if room[new_r][new_c] != 1 and [new_r, new_c] not in cleaned:
        cleaned.append([new_r, new_c])
        r, c, d = new_r, new_c, new_d
        turns = 0
        print('left', cleaned)
    elif turns == 4:
        new_r, new_c, new_d = go_back(r, c, d)
        if room[new_r][new_c] != 1:
            if [new_r, new_c] not in cleaned:
                cleaned.append([new_r, new_c])
            r, c = new_r, new_c
            print('back', cleaned)
        else:
            break

print(len(cleaned))