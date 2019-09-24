#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-09-23 23:53:32
# @Author  : Racterub (Racter Liu) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT

from math import sqrt

a = int(input("Input a:")) #測資: 5
b = int(input("Input b:")) #測資: 12
c = int(input("Input c:")) #測資: 13

s = (a + b + c)/2
area = sqrt(s*(s-a)*(s-b)*(s-c))
print(area)
#輸出: 30.0
