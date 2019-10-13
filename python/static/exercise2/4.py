#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-13 14:30:52
# @Author  : Racterub (Racter Liu) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT

data = int(input("Input your monthNumber")) #測資 8

if 1 <= data <= 2 or data == 12:
    print("Winter")
elif 3 <= data <= 5:
    print("Spring")
elif 6 <= data <= 8:
    print("Summer")
elif 9 <= data <= 11:
    print("Autumn")
else:
    print("Wrong input")

#測資 Summer