def solution(n, weak, dist):
    answer = None
    bet = []
    for i in range(len(weak)-1):
        bet.append(weak[i+1] - weak[i])
    bet.append(n-weak[-1])
    
    count = 0
    chunk = 0
    # 모든 지점에서 한 번씩 시작해본다
    for x in range(len(bet)):
        # 순서 다시 나열
        new_bet = bet[x:] + bet[:x]
        print('새로만든 것: ', new_bet)
        new_dist = dist
        # 가장 멀리 걷는 친구가 걸을 거리
        for i in range(len(new_bet)):
            if len(new_dist) == 0:
                    answer = -1
                    break
            elif chunk + new_bet[i] < new_dist[-1]:
                chunk += new_bet[i]
            else:
                count += 1
                chunk = new_bet[i]
                new_dist.pop()
        if answer == None or count < answer:
            answer = count
    
                
    return answer

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))