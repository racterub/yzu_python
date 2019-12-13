#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-12-12 10:50:52
# @Author  : Racter Liu (racterub) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT


sym_table = {"I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 60,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 600,
            "M": 1000}


data = int(input(": ")) #Input data
ans = '' # Answer
val = list(sym_table.values()) #Get table values in list
key = list(sym_table.keys()) #Get table keys in list


'''
用 sym_table 的值做迴圈
如果 data 大於 當前 sym_table 的 value, data 減掉該 value, ans 加上該 value 對應的羅馬數字
'''
for i in range(len(val)):
    while (data >= val[i]):
        data -= val[i]
        ans += key[i]

print(ans)