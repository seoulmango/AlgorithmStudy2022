def solution(N, stages):
    answer = []
    crt_stage = []
    failure = []
    for i in range(1, N+2):
        crt_stage.append(0)
    for stage in stages:
        crt_stage[stage-1] += 1
    ppl_left = len(stages)
    i = 1
    for crt in crt_stage:
        if ppl_left == 0:
            failure.append((i, 0))
        else:
            failure.append((i, crt/ppl_left))
        ppl_left -= crt
        i += 1
        if i == len(crt_stage):
            break
    failure.sort(reverse=True, key=lambda stage: stage[1])
    for fail in failure:
        answer.append(fail[0])
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))