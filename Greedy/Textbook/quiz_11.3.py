# 같이 연속되는 것은 하나로 본다

s = input()

new_s = s[0]

# 연속되는 값을 전부 삭제하여 새로운 str에 저장
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        new_s += s[i]

# 0과 1중 더 수가 적은 것을 선택
print(min(new_s.count('0'), new_s.count('1')))