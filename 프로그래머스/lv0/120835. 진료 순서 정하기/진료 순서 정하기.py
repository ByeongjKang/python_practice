def solution(emergency):
    order = dict(enumerate(emergency))
    order = sorted(order.items(), key = lambda x: x[1])
    return [abs(x[0]-len(order)) for x in order]