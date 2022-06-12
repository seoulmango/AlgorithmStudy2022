# str 값으로 숫자를 받는다
n = input()
digits = []

# 각 자릿수를 숫자로 치환해 리스트에 저장
for digit in n:
    digits.append(int(digit))

# 가장 큰 자릿수부터 시작
ans = digits[0]

# 곱과 덧셈 비교하며 큰 값을 저장
for i in range(1, len(digits)):
    if ans * digits[i] >= ans + digits[i]:
        ans *= digits[i]
    else:
        ans += digits[i]

print(ans)