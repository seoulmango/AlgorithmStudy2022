import sys
input = sys.stdin.readline

n = int(input())
waitinglist = list(map(int, input().split()))

# 수가 가장 큰 사람부터 1씩 더함
waitinglist.sort(reverse=True)

sum = 0

for i in range(1, len(waitinglist)+1):
    sum += waitinglist[i-1] * i

print(sum)