def solution(s):
    answer = ''
    s = s.lower()
    for i in range(len(s)) :
        if i == 0 :
            if s[i].isalpha() == 1 :
                answer += s[i].upper()
            else :
                answer += s[i]
        else :
            if s[i].isalpha() == 1 and s[i-1] == ' ' :
                answer += s[i].upper()
            else :
                answer += s[i]
    return answer