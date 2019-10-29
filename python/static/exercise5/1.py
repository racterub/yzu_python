#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-29 19:18:08
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

s1 = input("S1: ")
s2 = input("S2: ")
answer = ''

#Find the shortest string
if len(s1) >= len(s2):
    length = len(s2)
    for i in range(length):
        answer += s1[i]
        answer += s2[i]
    answer += s1[length:]
else:
    length = len(s1)
    for i in range(length):
        answer += s1[i]
        answer += s2[i]
    answer += s2[length:]

print(answer)