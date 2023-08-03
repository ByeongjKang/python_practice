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