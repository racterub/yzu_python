#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-11-26 00:32:09
# @Author  : Racter Liu (racterub) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT


f = open("10co2008CO_err.txt")
data = f.readlines()[1:]


maxinium = 0
for i in data:
    tmp_max = i.strip().split('\t')
    try:
        tmp_max = tmp_max[2]
        try:
            int_tmp_max = float(tmp_max)
            if int_tmp_max > maxinium:
                maxinium = int_tmp_max
        except ValueError:
            pass
    except IndexError:
        pass

print(maxinium)