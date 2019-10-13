#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-13 14:21:43
# @Author  : Racterub (Racter Liu) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT

data = int(input("Input your dateNumber:")) #測資: 6


if data == 0:
    print("Sunday")
elif data == 1:
    print("Monday")
elif data == 2:
    print("Tuesday")
elif data == 3:
    print("Wednesday")
elif data == 4:
    print("Thursday")
elif data == 5:
    print("Friday")
elif data == 6:
    print("Saturday")
else:
    print("Wrong input!")

#輸出 Saturday