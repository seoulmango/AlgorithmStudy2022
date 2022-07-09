# 가사 검색
# 프로그래머스 카카오 신입 공채 1차
# programmers.co.kr/learn/courses/30/lessons/60060

def solution(words, queries):
    answer = []
    queries_len = [len(q) for q in queries]
    words_len = [len(w) for w in words]
    
    for q in range(len(queries)):
        count = 0
        query = queries[q]
        for w in range(len(words)):
            # 길이가 같을 경우에만
            if queries_len[q] != words_len[w]:
                continue
            else:
                # ?가 전부일 때
                if query[0] == '?' and query[-1] == '?':
                    count += 1
                # abc????
                elif query[-1] == '?':
                    for i in range(queries_len[q]):
                        # ? 만나면 그만 세기
                        if query[i]=='?':
                            count += 1
                            break
                        # 다른 글자 만나면 그만 세기
                        elif query[i] != words[w][i]:
                            break
                    # 결격 사유 없으면 세기
                    else:
                        count += 1
                # ???abc
                elif query[0] == '?':
                    for i in range(-1, -queries_len[q] - 1, -1):
                        if query[i]=='?':
                            count += 1
                            break
                        # 다른 글자 만나면 그만 세기
                        elif query[i] != words[w][i]:
                            break
                    # 결격 사유 없으면 세기
                    else:
                        count += 1
        answer.append(count)

    return answer