def solution(s):
    answer = []
    if len(s)%2 == 1 :
        return 0
    for i in range(0,len(s)) :
        if len(answer) == 0 :
            answer.append(s[i])
        else :
            if s[i] == answer[-1] :
                answer.pop()
            else :
                answer.append(s[i])
    if len(answer) == 0 :
        return 1
    else :
        return 0