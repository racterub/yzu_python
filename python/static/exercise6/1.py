#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-11-13 10:09:42
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

import math

def validate_triangle():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    data_list = [a,b,c]
    data_list.sort()


    if (data_list[2] ** 2 ) == (data_list[0] ** 2 + data_list[1] ** 2):
        return True
    else:
        return False

print(validate_triangle())