def solution(str1, str2):
    li1 = [ str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha() ]
    li2 = [ str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha() ]
    union_set = set(li1)|set(li2)
    intersection_set = set(li1)&set(li2)
    union = []
    for x in union_set :
        if li1.count(x)>=li2.count(x) :
            temp = li1.count(x)
            while temp > 0 :
                union.append(x)
                temp -= 1
        else :
            temp = li2.count(x)
            while temp > 0 :
                union.append(x)
                temp -= 1
    intersection = []
    for y in intersection_set :
        if li1.count(y)>=li2.count(y) :
            temp = li2.count(y)
            while temp > 0 :
                intersection.append(y)
                temp -= 1
        else :
            temp = li1.count(y)
            while temp > 0 :
                intersection.append(y)
                temp -= 1
    if len(union) == 0 and len(intersection) == 0 :
        answer = 1
    else :
        answer = len(intersection)/len(union)
    return (answer*65536)//1