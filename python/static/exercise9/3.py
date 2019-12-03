#!/usr/bin/env python3


def alter(lst1, lst2):
    if len(lst1) > len(lst2):
        lst3 = []
        length = len(lst2)
        for i in range(length):
            lst3.append(lst1[i])
            lst3.append(lst2[i])
        lst3 += lst1[length:]
    else:
        lst3 = []
        length = len(lst1)
        for i in range(length):
            lst3.append(lst1[i])
            lst3.append(lst2[i])
        lst3 += lst2[length:]

    return lst3

print(alter([1,2,3], [4,5,6,7,8]))