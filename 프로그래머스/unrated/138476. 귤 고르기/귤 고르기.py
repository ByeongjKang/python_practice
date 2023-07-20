import operator

def solution(k, tangerine):
    table_of_tangerine = {}
    for key in tangerine :
        if key in table_of_tangerine :
            table_of_tangerine[key] += 1
        else :
            table_of_tangerine[key] = 1
    num = sorted(table_of_tangerine.items(), key=lambda x: x[1], reverse=True)
    temp = 0
    count = 0
    for key in num :
        temp += key[1]
        count += 1
        if temp >= k :
            return count
    
    
    
    '''    
def solution(k, tangerine):
    size_of_tangerine = set(tangerine)
    number_of_tangerine = []
    for key in size_of_tangerine :
        number_of_tangerine.append(tangerine.count(key))
    number_of_tangerine.sort(reverse = True)
    temp = 0
    count = 0
    for key2 in number_of_tangerine :
        temp += key2
        count += 1
        if temp >= k :
            return count
            
            
import operator

def solution(k, tangerine):
    size_of_tangerine = set(tangerine)
    table_of_tangerine = {}
    for key in size_of_tangerine :
        table_of_tangerine[key] = tangerine.count(key)
    num = sorted(table_of_tangerine.items(), key=operator.itemgetter(1), reverse=True)
    temp = 0
    count = 0
    for key in num :
        temp += key[1]
        count += 1
        if temp >= k :
            return count
    '''