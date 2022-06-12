n = int(input())

wordlist = []
for _ in range(n):
    wordlist.append(input().zfill(8))

# 각 단어의 알파벳을 단위순으로 큰 숫자 부여하기

alphabets = []

for i in range(8):
    for word in wordlist:
        if word[i] != "0" and word[i] not in alphabets:
            alphabets.append(word[i])


word_to_num = {}
biggest = 9

for alphabet in alphabets:
    word_to_num[alphabet]=biggest
    biggest -= 1

numlist = []
for word in wordlist:
    number = ""
    for alphabet in word:
        if alphabet != '0':
            number += str(word_to_num[alphabet])
    number = int(number)
    numlist.append(number)

print(sum(numlist))