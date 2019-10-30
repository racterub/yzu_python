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



string = input(': ') #測資: Hello-123-World!

alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

answer = ''
tmp = ''
for i in range(len(string)):
    if string[i] in alphabets:
        tmp += string[i]
    else:
        answer += tmp[::-1]
        tmp = ''
        answer += string[i]
answer += tmp[::-1]

print(answer)
#輸出: olleH-123-dlroW!