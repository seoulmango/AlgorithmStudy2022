def solution(s):
    answer = None

    s_length = len(s)

    # 압축 단위가 2~"문자의 길이의 반"이다
    for chunk_length in range(1, s_length//2+1):
        # 해당 단위로 압축했을 때의 문자열
        new_s = ""
        count = 1
        for i in range(s_length//chunk_length+1):
            # 현재 단위와 뒤의 단위가 같을 경우, count + 1 한다.
            if s[i*chunk_length:(i+1)*(chunk_length)] == s[(i+1)*chunk_length:(i+2)*(chunk_length)]:
                count += 1
            # 현재 단위와 뒤의 단위가 다를 경우, new_s에 값을 추가해준다.
            else:
                # 같은 단위가 연속적으로 있었을 경우, 압축해서 추가한다.
                if count > 1:
                    new_s += str(count)+s[i*chunk_length:(i+1)*(chunk_length)]
                    count = 1
                # 같은 단위가 연속적으로 없었다면 그냥 추가한다.
                else:
                    new_s += s[i*chunk_length:(i+1)*(chunk_length)]
        
        # 새롭게 압축한 값이 기존의 답보다 더 짧으면 답을 갱신한다.
        if answer is None or answer > len(new_s):
            answer = len(new_s)

    # 예외처리) 압축 단위가 1일 때
    if len(s) == 1:
        answer = 1

    return answer