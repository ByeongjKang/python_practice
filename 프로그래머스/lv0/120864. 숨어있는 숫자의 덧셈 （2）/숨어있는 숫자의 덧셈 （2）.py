def solution(my_string):
    temp = ''
    s = 0
    for key in my_string :
        if key.isdigit() :
            temp += key
        elif temp != '' :
            s += int(temp)
            temp = ''
    if temp != '' :
        s += int(temp)
    return s
"""훨씬 나은 풀이
def solution(my_string) :
    n = ''.join( x for x in my_string if x.isdigit() else '')
    return sum( i for i in n.split())"""