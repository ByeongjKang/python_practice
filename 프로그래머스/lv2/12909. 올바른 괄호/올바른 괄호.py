def solution(s):
    if len(s)%2 == 1 :
        return False
    count = 0
    for key in s :
        if key == '(' :
            count += 1
        else :
            count -= 1
            if count < 0 :
                return False
    if count == 0 :
        return True
    else :
        return False
    
    """answer = []
    if len(s)%2 == 1 :
        return False
    for i in range(len(s)) :
        if len(answer) == 0 :
            answer.append(s[i])
        else :
            if answer[i-1] + s[i] == '()' :
                answer.pop()
    if len(answer) == 0 :
        return True
    else :
        return False"""