def solution(sizes):
    maximum = 0
    other = 0
    for i in range(len(sizes)) :
        if maximum < max(sizes[i]) :
            maximum = max(sizes[i])
            other = min(sizes[i])
            idx = i
    rep = sizes[idx]
    del sizes[idx]
    maxofmin = 0
    for j in range(len(sizes)) :
        if maxofmin < min(sizes[j]) :
            maxofmin = min(sizes[j])
    if maximum * maxofmin < maximum * other :
        return maximum * other
    else :
        return maximum * maxofmin
