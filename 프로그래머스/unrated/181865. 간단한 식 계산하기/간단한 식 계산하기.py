def solution(binomial):
    a, op, b = map(str,binomial.split())
    a = int(a)
    b = int(b)
    if op == '+' :
        return a + b
    elif op == '*' :
        return a * b
    else :
        return a - b
