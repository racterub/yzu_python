#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-11-26 01:20:25
# @Author  : Racter Liu (racterub) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT

def has_dups(data):
    for i in data:
        if data.count(i) > 1:
            return True
        else:
            return False

print(has_dups([1,2,3,4,5]))
print(has_dups([1,2,1,3,4,5]))