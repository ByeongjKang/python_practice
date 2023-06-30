def solution(price, money, count):
    fee = sum(price*N for N in range(1,count+1))
    return fee - money if fee > money else 0