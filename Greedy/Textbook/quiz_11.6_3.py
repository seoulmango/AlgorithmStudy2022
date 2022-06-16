def solution(food_times, k):
    answer = 0
    time = 0
    plate_idx = 0
    food_num = len(food_times)
    tries = 0
    while True:
        if food_times.count(0) == food_num:
            answer = -1
            break

        # idx가 넘어가면 첫번째 음식으로 돌아오기
        elif plate_idx == food_num:
            plate_idx = 0

        # 다 먹었다면 다음 음식으로
        elif food_times[plate_idx] == 0:
            plate_idx += 1

        # 먹을 수 있는 음식이라면 먹기
        else:
            food_times[plate_idx] -= 1
            time += 1
            # 시간 초과 시, 먹을 수 있는 다음 음식 앞에서 break
            if time == k+1:
                answer = plate_idx + 1
                break
            plate_idx += 1        
    return answer