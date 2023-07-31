def solution(my_string):
    my_string = my_string.lower()
    my_string = sorted(my_string)
    return ''.join( x for x in my_string)