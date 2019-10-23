#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-23 19:31:54
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

data = int(input("Input your upper range:")) #測資: 10

if data == 0:
    print("Exiting")
    exit()
elif data < 0:
    print("Negative range")
    exit()
else:
    answer = 0
    for i in range(1, data+1):
        fac = 1
        for j in range(1, i+1):
            fac *= j
        print("Running: {}, factoral: {}".format(i, fac)) #For debugging 幫你印出當前的階乘數字和階乘結果，只是給你看目前跑到哪
        answer = answer + fac
    print(answer)

#輸出 4037913