#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-09-23 23:53:32
# @Author  : Racterub (Racter Liu) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT

from math import sqrt

a, b, c = [int(i) for i in input("Input your triangle (a b c):").split(" ")]

s = a + b + c
area = sqrt(s*(s-a)*(s-b)*(s-c))
print(area)
