#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-29 20:05:04
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

string = input(': ')

answer = ''
tmp = ''
for i in range(len(string)):
    if string[i].isalpha():
        tmp += string[i]
    else:
        answer += tmp[::-1]
        tmp = ''
        answer += string[i]
answer += tmp[::-1]

print(answer)