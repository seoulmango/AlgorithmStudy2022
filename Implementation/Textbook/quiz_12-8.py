s = input()

sl = []
sum = 0

for alphabet in s:
    # 정수로 표현 가능하다면 합 더하기
    try:
        sum += int(alphabet)
    # 에러가 뜬다면 문자열 리스트에 넣기
    except:
        sl.append(alphabet)

# 문자 정렬
sl.sort()

# 합친 이후 출력하기
for x in sl:
    print(x, end="")
if sum != 0:
    print(sum)