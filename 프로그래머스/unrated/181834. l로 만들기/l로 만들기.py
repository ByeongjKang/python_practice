def solution(myString):
    for key in myString :
        if key < 'l' :
            myString = myString.replace(key,'l',1)
    return myString