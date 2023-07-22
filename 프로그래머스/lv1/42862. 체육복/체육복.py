def solution(n, lost, reserve):
    notMine = sorted([ x for x in lost if x not in reserve ])
    canRent = sorted([ x for x in reserve if x not in lost ])
    count = 0
    for key in notMine :
        if key-1 in canRent :
            canRent.remove(key-1)
            count += 1
        elif key+1 in canRent :
            canRent.remove(key+1)
            count += 1
    return n - len(notMine) + count



