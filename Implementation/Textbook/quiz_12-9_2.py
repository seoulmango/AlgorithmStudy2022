def compress(s, chunk_length):
    words = [s[i:i+chunk_length] for i in range(0, len(s), chunk_length)]

    res = []
    count = 1
    for cur, next in zip(words, words[1:]+[""]):
        if cur == next:
            count += 1
        else:
            res.append([count, cur])
            count = 1
    
    ans = sum(len(cur) + (len(str(count)) if count>1 else 0) for count, cur in res)
    return ans

def solution(s):
    return min(compress(s, chunk_length) for chunk_length in list(range(1,len(s)//2+1))+[len(s)])
