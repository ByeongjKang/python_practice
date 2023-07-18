def solution(nums):
    di = len(nums)//2
    result = []
    N = list(set(nums))
    count = 0
    for key in N :
        hashh = list(divmod(key, di))
        if hashh not in result :
            result.append(hashh)
    if len(result) > di :
        return di
    else :
        return len(result)