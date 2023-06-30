def solution(my_strings, parts):
    answer = ''
    idx = 0
    for key in my_strings :
        answer += key[parts[idx][0]:parts[idx][1]+1]
        idx += 1
    return answer