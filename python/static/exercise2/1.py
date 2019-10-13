#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-13 12:15:14
# @Author  : Racterub (Racter Liu) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT

x = int(input('x: ')) #測資: 1
y = int(input('y: ')) #測資: 2
z = int(input('z: ')) #測資: 3

_avg = (x+y+z)/3 

_min = x
if y < _min:
    _min = y
    if z < _min:
        _min = z
        _max = x
    if x > z:
        _max = x
    else:
        _max = z
elif z < _min:
    _min = z
    _max = y
else:
    if y > z:
        _max = y
    else:
        _max = z

print(_min, _avg, _max)
#輸出: 1, 2, 3