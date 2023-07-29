def solution(myString, pat):
    str1 = myString.replace('A', 'b')
    str2 = str1.replace('B', 'A')
    str2 = str2.upper()
    if pat in str2 :
        return 1
    else : 
        return 0