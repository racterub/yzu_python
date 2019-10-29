#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-29 20:34:20
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

string = input("Input your string: ")

answer = ''
tmp = ''
for i in range(len(string)):
    if string[i] != ' ':
        tmp += string[i]
    else:
        answer += tmp[::-1]
        tmp = ''
        answer += ' '

answer += tmp


print(answer)