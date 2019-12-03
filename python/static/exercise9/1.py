#!/usr/bin/env python3


def has_dups(data):
    for i in data:
        if data.count(i) > 1:
            return True
        else:
            return False

print(has_dups([1, 2, 3]))
print(has_dups([1,1,2,3]))