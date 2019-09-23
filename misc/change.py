#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-09-23 16:24:15
# @Author  : Racterub (Racter Liu) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT

price = int(input("Input the price: "))
data = 100 - price

fifty = data // 50
fifty_trash = data % 50
ten = fifty_trash // 10
ten_trash = fifty_trash % 10
five = ten_trash // 5
one = ten_trash % 5

print("50: ", fifty,"10: ", ten,"5 :", five,"1: ", one)