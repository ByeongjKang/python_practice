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