#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-11-13 12:32:14
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

def sum_digits():
    data = input(": ").strip()
    result = 0
    for i in str(data):
        result += int(i)
    return result

print(sum_digits())