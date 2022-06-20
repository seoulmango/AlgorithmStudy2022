s = [input() for i in range(5)]
max_length = 0
 
if len(s) > max_length:
    max_length = len(s)
 
# 방법 1
# for i in range(max_length):
#     for j in range(len(s)):
#         if i >= len(s[j]):
#             continue
#         else:
#             print(s[j][i], end='')
 
# 방법 2
for i in range(max_length):
    for j in s:
        if i >= len(j):
            print(j[i], end='')