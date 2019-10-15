#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-09-23 23:43:18
# @Author  : Racterub (Racter Liu) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT

data = int(input("Input your text: ")) #測資: (1) 11211 or (2) 12331

a = data % 10
data = data // 10
b = data % 10
data = data // 10
c = data % 10
data = data // 10
d = data % 10
e = data // 10

if (e == a and b == d):
    print("It's a palindrome!") #(1) 輸出
else:
    print("It's not a palindrome!") #(2) 輸出


