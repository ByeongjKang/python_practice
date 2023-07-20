import itertools

def solution(babbling):
    can_speak = ['aya', 'ye', 'woo', 'ma']
    can_speak2 = list(itertools.permutations(can_speak,2))
    can_speak3 = list(itertools.permutations(can_speak,3))
    can_speak4 = list(itertools.permutations(can_speak,4))
    candidate = can_speak
    for key in can_speak2 :
        candidate.append(''.join( x for x in key))
    for key in can_speak3 :
        candidate.append(''.join( x for x in key))
    for key in can_speak4 : 
        candidate.append(''.join( x for x in key))
        
    count = 0
    for key in babbling :
        if key in candidate :
            count += 1
    return count