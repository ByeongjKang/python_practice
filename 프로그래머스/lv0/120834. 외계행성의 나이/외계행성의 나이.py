def solution(age):
    age = str(age)
    return ''.join( chr(97+int(x)) for x in age )