#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-16 00:03:43
# @Author  : Racterub (Racter Liu) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT


def fib(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib(n-1) + fib(n-2)

data = int(input("Input fibonacci sequence:")) #測資: 8

print(fib(data))
#輸出: 21