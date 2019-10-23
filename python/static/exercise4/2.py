#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-23 19:10:24
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

ROW = 10

print("Printing pattern C:")
for i in range(ROW):
    print(' '*i, end='')
    print('*'*( ROW-i))

print("Printing pattern D:")
for i in range(ROW):
    print(' '*(ROW-i-1), end='')
    print('*'*(i+1))
