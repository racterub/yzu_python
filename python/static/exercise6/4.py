#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-11-13 12:32:54
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

def LeibnizPi(n):
    sigma = 0
    for i in range(1, n+1):
        sigma += ((-1)**(i-1))/(2*i-1)
    sigma *= 4
    return sigma

print(LeibnizPi(1000))
