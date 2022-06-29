n = int(input())
nlist=[]
for _ in range(n):
    nlist.append(int(input()))
nlist.sort()

ans = nlist[0]*(n-1)
if n == 1:
    print(0)
else:
    for i in range(1, n):
        ans += nlist[i]*(n-i)
    print(ans)

# 틀린 이유: 작은 것 두 개의 합이 3번째+4번째로 작은 수의 합보다 더 큰 수가 될 수도 있다..!
# ex) 5, 50, 51, 52 순으로 있을 때
# 5+50이 51+52보다 커진다. 그러므로 위의 코드는 올바르지 못하다.