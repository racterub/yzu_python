#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-29 19:53:54
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

string = input("Input your string: ")
string_len = len(string)

answer = []
for i in range(string_len):
    a = string[i]
    for j in range(string_len):
        b = string[j]
        for k in range(string_len):
            c = string[k]
            if (a != b and b != c and a != c):
                answer.append(a+b+c)


print(', '.join(answer))