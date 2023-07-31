def solution(num, k):
    strnum = str(num)
    for i in range(len(strnum)) :
        if strnum[i] == str(k) :
            return i+1
    return -1