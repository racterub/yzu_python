#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-09-08 23:26:26
# @Author  : Racterub (Racter Liu) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT

data = int(input("Input data: ")) #測資: 42139

a = data % 10
data = data // 10
b = data % 10
data = data // 10
c = data % 10
data = data // 10
d = data % 10
data = data // 10
e = data % 10

print(e, d, c, b, a, sep="   ")
#輸出: 4   2   1   3   9