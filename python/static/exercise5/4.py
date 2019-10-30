#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-29 19:53:54
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

'''
就老師上課教的那樣
i 是第一個數字
j 是第二個數字
k 是第三個數字
想成是高中機率組合，在找機率就是ㄌ，三個字不重複
'''


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


for i in answer:
    print(i, end=" ")