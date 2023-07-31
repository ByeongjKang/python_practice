def solution(my_string, s, e):
    a = my_string[s:e+1][::-1]
    return my_string[:s]+''.join(x for x in a)+my_string[e+1:]