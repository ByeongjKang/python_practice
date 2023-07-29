def solution(my_string):
    l = list(my_string)
    a = ''
    for key in my_string :
        if key.islower() :
            a += key.upper()
        else :
            a += key.lower()
    return a