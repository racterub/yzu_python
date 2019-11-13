#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-11-04 11:02:19
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

def check_digit(pwd):
    ok = False
    data = '$#@'
    for i in pwd:
        if i in data:
            ok = True
            break
    return ok