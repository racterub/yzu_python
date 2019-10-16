#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-15 23:13:19
# @Author  : Racterub (Racter Liu) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT

data = int(input("Input your data:")) #測資: 2

answer = 1
for i in range(1, 101):
    fac = 1
    tmp = 1
    while tmp <= i:
        fac *= tmp
        tmp += 1
    eq = data**i/fac
    answer = answer + eq
print(answer)
#輸出: 7.389056098930649