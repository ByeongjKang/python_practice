def solution(n):
    binary_n = bin(n)
    list_binary_n = list(bin(n)[2:])
    while True :
        n += 1
        if binary_n.count('1') == bin(n).count('1') :
            next_n = bin(n)
            break
            
    return int(next_n,2)