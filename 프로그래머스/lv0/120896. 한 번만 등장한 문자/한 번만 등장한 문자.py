from collections import Counter
def solution(s):
    dic = Counter(s)
    dic = sorted(dic.items())
    return ''.join( x[0] for x in dic if x[1]==1 )