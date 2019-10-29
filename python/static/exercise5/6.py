#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-29 20:34:20
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

string = input("Input your string: ")

answer = [i[::-1] for i in string.split(' ')]

print(' '.join(answer))