# 회의가 n개 있을 때, 각 회의의 i 번째를 첫 번째 회의 시작 시간으로 설정해본다.
# 다음 인덱스의 회의를 시작할 수 있으면 바로 시작한다.
# 그렇게 해서 최대한 많은 회의를 할 수 있는 경우의 수를 뽑는다.
# 회의를 정렬할 때, 1. 시작 시간 순 2. 끝나는 시간 순(회의의 지속 시간)으로 정렬되므로
# Greedy의 조건에 부합한다.
import sys
input = sys.stdin.readline

n = int(input())
all_meetings = []

for _ in range(n):
    all_meetings.append(list(map(int, input().split())))

# 회의 시간을 시작 순서 시간/끝나는 순서 시간 순으로 정렬한다.
all_meetings.sort()

meetings = [all_meetings[0]]

# 같은 시간에 시작하는 것 중, 가장 짧은 것만 남긴다.
# 같은 시간에 시작하고 끝나는 것들도 추가한다. 
for i in range(1, len(all_meetings)):
    if all_meetings[i][0] == all_meetings[i][1]:
        meetings.append(all_meetings[i])
    elif all_meetings[i][0] != all_meetings[i-1][0] or all_meetings[i-1][0] == all_meetings[i-1][1]:
        meetings.append(all_meetings[i])

# 최대 가능한 답을 설정
ans = 0
n = len(meetings)
next_meetings = []

for i in range(n-1):
    # 시작하는 회의를 iterate
    last_meeting = meetings[i]
    count = 1

    # 시작하는 회의가 전의 조합 중에 있을 경우, 건너뛴다.
    if last_meeting in next_meetings:
        continue

    # 시작하는 회의 오른쪽 회의들 탐색
    for x in range(i+1, n):
        # 만약 다음 회의로 시작할 수 있다면, count+1, 그리고 마지막 회의를 최신화한다.
        if last_meeting[1] <= meetings[x][0]:
            count += 1
            last_meeting = meetings[x]
            next_meetings.append(last_meeting)
    
    # 정답 최신화
    if count > ans:
        ans = count

print(ans)