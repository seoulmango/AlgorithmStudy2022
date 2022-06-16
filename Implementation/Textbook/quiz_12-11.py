from collections import deque

n = int(input())

k = int(input())

klist= []
for _ in range(k):
    klist.append(list(map(int, input().split())))

l = int(input())

llist = []
for _ in range(l):
    llist.append(list(input().split()))

direction = 4

klist = deque(klist)
llist = deque(llist)

time = 0
while True:
    if direction == 4:
        pass