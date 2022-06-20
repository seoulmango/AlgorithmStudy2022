def solution(n, build_frame):
    answer = []
    
    for build in build_frame:
        x = build[0]
        y = build[1]
        a = build[2]
        b = build[3]
        
        # 설치할 때
        if b == 1:
            # 기둥
            if a == 0:
                # 짓는 조건 충족
                if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                    answer.append([x, y, a])
            # 보
            if a == 1:
                # 짓는 조건 충족
                if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                    answer.append([x, y, a])
        # 삭제할 때
        if b == 0:
            # 기둥
            if a == 0:
                # 위에 기둥 있을 때
                if [x, y+1, 0] in answer:
                    if y+1 == 0 or [x-1, y+1, 1] in answer or [x, y+1, 1] in answer:
                        pass
                    else:
                        continue
                # 오른쪽에 보가 있을 때
                if [x, y+1, 1] in answer:
                    if [x+1, y, 0] in answer or ([x-1, y+1, 1] in answer and [x+1, y+1, 1] in answer):
                        pass
                    else:
                        continue
                # 왼쪽에 보가 있을 때
                if [x-1, y+1, 1] in answer:
                    if [x-1, y, 0] in answer or ([x-2, y+1, 1] in answer and [x, y+1, 1] in answer):
                        pass
                    else:
                        continue
                answer.remove([x, y, a])
            # 보
            if a == 1:
                # 왼쪽 위에 기둥 있을 때
                if [x, y, 0] in answer:
                    if y == 0 or [x-1, y, 1] in answer or [x, y-1, 0] in answer:
                        pass
                    else:
                        continue
                # 오른쪽 위에 기둥 있을 때
                if [x+1, y, 0] in answer:
                    if y == 0 or [x+1, y, 1] in answer or [x+1, y-1, 0] in answer:
                        pass
                    else:
                        continue
                # 왼쪽에 보가 있을 때
                if [x-1, y, 1] in answer:
                    if [x-1, y-1, 0] in answer or [x, y-1, 0] in answer:
                        pass
                    else:
                        continue
                # 오른쪽에 보가 있을 때
                if [x+1, y, 1] in answer:
                    if [x+1, y-1, 0] in answer or [x+2, y-1, 0] in answer:
                        pass
                    else:
                        continue
                answer.remove([x,y,a])
    answer.sort()
    return answer


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))