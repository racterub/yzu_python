#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-12-12 11:44:10
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

data = input(": ")[::-1] #Input data
ans = 0 #Answer
tmp = None #上一個字

'''
因為羅馬數字的排法，所以先把它全部顛倒，然後一個字一個字看，對 ans 加上該羅馬數字對應的數字，並且將上一個讀過的字留起來做比對，如果當前字元比上一個小，
則將 ans 減兩次
'''
for i in data:
    if (tmp and sym_table[i] < tmp):
        ans -= 2*sym_table[i]
    ans += sym_table[i]
    tmp = sym_table[i]

print(ans)

