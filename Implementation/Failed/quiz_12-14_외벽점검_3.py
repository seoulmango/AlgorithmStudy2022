from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+ n)
    answer = len(dist) + 1

    # 0부터 length-1까지의 위치를 시작점으로 설정
    for start in range(length):
        # 친구 나열 가능한 모든 경우 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입 친구 수
            # 해당 친구가 점검 가능한 마지막 위치
            position = weak[start] + friends[count-1]
            for index in range(start, start + length):
                # 점검할 수 있는 위치 벗어날 때
                if position < weak[index]:
                    count += 1 # 새 친구 투입
                    if count > len(dist): # 투입할 친구가 없을 때
                        break
                    position = weak[index] + friends[count-1]
            answer = min(answer, count)
        if answer > len(dist):
            return -1
        return answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))