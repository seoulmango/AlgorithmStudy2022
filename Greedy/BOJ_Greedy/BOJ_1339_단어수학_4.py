n = int(input())

# 단어들을 저장
wordlist = []
for _ in range(n):
    wordlist.append(input())

# 단어를 계수 * 알파벳의 형태로 바뀐 뒤, 그 값들을 dict형태로 저장.
word_dict = {}
for word in wordlist:
    a = len(word)
    for alphabet in word:
        a -= 1
        if alphabet in word_dict.keys():
            word_dict[alphabet] += 10**a
        else:
            word_dict[alphabet] = 10**a

# 계수를 큰 순서대로 정렬
word_dict_values = list(word_dict.values())
word_dict_values.sort(reverse=True)

# 계수가 큰 알파벳부터 9, 8, 7 ... 순으로 부여. 합 계산하여 출력.
sum = 0
biggest_digit = 9
for num in word_dict_values:
    num *= biggest_digit
    biggest_digit -= 1
    sum += num

print(sum)