n = input()

# 숫자를 왼쪽 오른쪽으로 나누어 str으로 저장
half = int(len(n)/2)
ln = n[:half]
rn = n[half:]

# 좌우 합 따로 구하기
lsum = 0
rsum = 0
for ld in ln:
    lsum += int(ld)
for rd in rn:
    rsum += int(rd)

# 결과 출력
if lsum == rsum:
    print('LUCKY')
else:
    print('READY')