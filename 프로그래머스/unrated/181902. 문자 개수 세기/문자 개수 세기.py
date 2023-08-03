def solution(my_string):
    cntList = []
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' :
        cntList.append(my_string.count(i))
    return cntList