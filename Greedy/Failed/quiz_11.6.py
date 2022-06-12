def solution(food_times, k):
    time = 0
    idx = 0

    while time < k:
        # 해당 음식이 0이면 다음 음식으로, 아니라면 먹기
        if food_times[idx] == 0:
            idx += 1
            continue
        else:
            food_times[idx] -= 1
            # 다음 음식으로 이동 준비
            idx += 1
            # 시간은 1초 흐름
            time += 1

        # 모든 음식을 다 먹었다면 break
        if food_times.count(0) == len(food_times):
            idx = -1
            break

        # idx가 끝이면 0으로 다시 돌아오기
        if idx == len(food_times):
            idx = 0

    return idx+1

print(solution([3, 1, 2], 5))