n = int(input())

wordlist = []
for _ in range(n):
    # 수의 최대 길이가 8이라고 문제에 명시돼 있음
    wordlist.append(input().zfill(8))

# 각 단어의 알파벳을 단위순으로 큰 숫자 부여하기
word_to_num = {}
nums = [i for i in range(10)]

idx_list = [[] for i in range(8) ]

for word in wordlist:
    for i in range(8):
        if word[i] != '0':
            idx_list[i].append(word[i])


idx_list_amount = [[] for i in range(8)]
word_num = {}
biggest = 9
i = -1
for idx in idx_list:
    i += 1
    for alphabet in idx:
        amount = idx.count(alphabet)
        if {amount : alphabet} not in idx_list_amount[i]:
            idx_list_amount[i].append({amount : alphabet})


print(idx_list_amount)
for tup in idx_list_amount:
    if tup[1] not in word_num.keys():
        word_num[tup[1]] = biggest
        biggest -= 1

numbers = []
for word in wordlist:
    number = ""
    for alphabet in word:
        if alphabet != '0':
            number += str(word_to_num[alphabet])
    number = int(number)
    numbers.append(number)

print(sum(numbers))