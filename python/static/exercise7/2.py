#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-11-18 23:52:14
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

f = open("golf.txt", "r").readlines()

for i in range(0, len(f), 2):
    print("Name: ", f[i].strip())
    print("Score: ", f[i+1].strip())
