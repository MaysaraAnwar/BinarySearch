def binarysearch (lis, target):
    left = 0
    right = length - 1
    while left <= right:
        midle = (left + right)/2
        if lis[midle] == target:
            return midle
        elif lis[midle] < target:
            return midle - 1
        else :
            return midle +1
    return -1
    