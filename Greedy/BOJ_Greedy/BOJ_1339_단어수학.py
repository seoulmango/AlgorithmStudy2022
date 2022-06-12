n = int(input())

wordlist = []
for _ in range(n):
    # 수의 최대 길이가 8이라고 문제에 명시돼 있음
    wordlist.append(input().zfill(8))

# 각 단어의 알파벳을 단위순으로 큰 숫자 부여하기
word_to_num = {}
nums = [i for i in range(10)]

for i in range(8):
    for word in wordlist:
        if word[i] != '0' and word[i] not in word_to_num.keys():
            word_to_num[word[i]] = nums[-1]
            del nums[-1]

numbers = []

for word in wordlist:
    number = ""
    for alphabet in word:
        if alphabet != '0':
            number += str(word_to_num[alphabet])
    number = int(number)
    numbers.append(number)

print(sum(numbers))