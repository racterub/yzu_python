#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-29 19:18:08
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

'''
先找出長度最小的字串，以他的長度為基準開一個 for loop ，然後前面先 s1 s2 互相填入 answer ，直到長度最小的字串結束，再將長度較長的字串的剩餘資料寫入 answer
'''


s1 = input("S1: ") #測資: hi
s2 = input("S2: ") #測資: hello
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
#輸出: hhiello