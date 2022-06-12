# 수학적인 풀이

# 첫 줄의 값 입력받기
n, m, k = map(int, input().split())

# 둘 째 줄의 값을 리스트 형태로 입력받기
numlist = list(map(int, input().split()))

# 오름차순으로 나열
numlist.sort()

# 리스트의 가장 큰 값과 둘 째로 큰 값 특정하기
first = numlist[-1]
second = numlist[-2]

# 수학 수식 계산하기
ans = first*(m//(k+1))*k + first*(m%(k+1)) + second*(m//(k+1))

print(ans)