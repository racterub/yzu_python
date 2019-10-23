#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-23 18:49:22
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

from math import sqrt

for i in range(1, 1000001):
    root = int(sqrt(i))
    if (root*root == i):
        data = i+268
        root_new = int(sqrt(data))
        if (root_new * root_new == data):
            print(i, end=" ")

#輸出 4356