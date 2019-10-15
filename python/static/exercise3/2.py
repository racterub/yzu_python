#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-15 22:19:17
# @Author  : Racterub (Racter Liu) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT

data = int(input("Input your number:"))

if data == 0:
    print("exit")
    exit()
elif data < 0:
    print("data is negative")
    exit()
else:
    answer = 1
    i = 1
    while i <= data:
        answer = answer * i
        i += 1
    print(answer)