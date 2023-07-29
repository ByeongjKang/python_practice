def solution(s):
    cnt_0 = 0
    cnt_change = 0
    while s != '1' :
        a = len(s)
        s = s.replace('0','')
        b = len(s)
        cnt_0 += (a-b)
        s = bin(b)[2:]
        cnt_change += 1
    return [cnt_change, cnt_0]
        