def solution(want, number, discount):
    to_sell_dict = {}
    day = 0
    for i in range(0,len(discount)-9) :
        for key in want :
            to_sell_dict[key] = discount[i:i+10].count(key)
        if dict(zip(want, number)) == to_sell_dict :
            day +=1
    return day