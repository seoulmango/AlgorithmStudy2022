wlist = []
for _ in range(5):
    wlist.append(input())

# 단어들 중 가장 긴 단어를 구한다.
longest_len = 0
for word in wlist:
    if len(word) > longest_len:
        longest_len = len(word)

# 가장 긴 단어의 자릿수 만큼 리스트를 만든다.
# 세로리스트 = [[첫 째 자리 알파벳들], [둘 째 자리 알파벳들], ... , [마지막 자리 알파벳들]]
vlist = []
for _ in range(longest_len):
    vlist.append([])
for word in wlist:
    for idx in range(len(word)):
        vlist[idx].append(word[idx])

# 세로리스트 속 알파벳들을 순서대로 출력한다
for col in vlist:
    for alphabet in col:
        print(alphabet, end="")