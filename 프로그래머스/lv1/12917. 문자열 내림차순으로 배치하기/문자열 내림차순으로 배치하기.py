def solution(s):
    answer = ''
    s_list = sorted(s, reverse=True)
    for i in s_list :
        answer += i
    return answer