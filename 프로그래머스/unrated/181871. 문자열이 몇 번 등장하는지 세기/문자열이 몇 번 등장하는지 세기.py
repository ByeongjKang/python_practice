def solution(myString, pat):
    slicedStr = [ myString[i:i+len(pat)] for i in range(0,len(myString)-len(pat)+1) ]
    return slicedStr.count(pat)