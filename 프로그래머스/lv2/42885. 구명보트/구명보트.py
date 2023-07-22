def solution(people, limit):
    people = sorted(people, reverse=True)
    count = 0
    for key in people :
        if people[-1] <= (limit-key) :
            people.pop(-1)
        count+=1
    return count