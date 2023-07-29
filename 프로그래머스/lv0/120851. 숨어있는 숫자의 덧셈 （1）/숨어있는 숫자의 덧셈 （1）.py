def solution(my_string):
    c = 0
    for key in my_string :
        if key.isdigit() :
            c += int(key)
    return c