def solution(my_string):
    a = my_string
    for key in ['a','e','i','o','u'] :
        a = a.replace(key, '')
    return a