def solution(n):
    s = str(n)
    l = list(s)
    c = 0
    for key in s :
        c += int(key)
    return c