def solution(strArr):
    lenList = []
    for key in strArr :
        lenList.append(len(key))
    group = set(lenList)
    return max(lenList.count(x) for x in group)