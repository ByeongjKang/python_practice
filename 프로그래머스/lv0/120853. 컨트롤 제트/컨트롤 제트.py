def solution(s):
    order = list(map(str,s.split()))
    stack = []
    for key in order :
        if key == 'Z' :
            stack.pop()
        else :
            stack.append(int(key))
    return sum(stack)