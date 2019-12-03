#!/usr/bin/env python3


def comb(lst1, lst2):
    tmp = []
    for i in lst1:
        if i not in lst2:
            tmp.append(i)
    for i in lst2:
        if i not in lst1:
            tmp.append(i)
    return sorted(tmp)

print(comb([4,3,2,6,2], [1,2,4,1,5]))