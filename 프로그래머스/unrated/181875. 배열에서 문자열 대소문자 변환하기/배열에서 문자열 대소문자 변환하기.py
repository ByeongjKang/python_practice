def solution(strArr):
    c = 0
    for key in (strArr) :
        if c%2 == 0 :
            strArr[c] = key.lower()
        else :
            strArr[c] = key.upper()
        c += 1
    return strArr