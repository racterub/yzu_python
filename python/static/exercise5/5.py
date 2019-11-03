#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-29 20:05:04
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

'''
做法同第六題
'''



string = list(input(': ')) #測資: Hello-123-World!



answer = ''
alpha = []
for i in range(len(string)):
    if string[i].isalpha():
        alpha.append(string[i])

for i in range(len(string)):
    if string[i].isalpha():
        string[i] = alpha.pop()


print(''.join(string))
#輸出: olleH-123-dlroW!