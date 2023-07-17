def solution(priorities, location):
    loca = [ 0 ] * len(priorities)
    loca[location] = 1
    count = 0
    while len(priorities) > 0 :
        if priorities[0] == max(priorities) :
            count += 1
            if loca[0] == 1 :
                return count
            priorities.pop(0)
            loca.pop(0)

            
        else :
            priorities.append(priorities[0])
            priorities.pop(0)
            loca.append(loca[0])
            loca.pop(0)
    return count