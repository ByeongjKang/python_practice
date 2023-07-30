def solution(myString):
    result = list(map(str,myString.split('x')))
    while '' in result :
        result.remove('')
    return sorted(result)