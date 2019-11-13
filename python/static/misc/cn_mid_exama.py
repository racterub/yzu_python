#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-11-04 10:22:34
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT


"""
題目:
給定兩輸入 s1, s2
將 s1 最左平移至最右，可平移多次，檢查是否和 s2 相同
輸入 exit 來結束程式

Example1:
s1 = 'abcde'
s2 = 'cdeab'

Answer: True

Example2:
s1 = 'abcde'
s2 = 'cdeba'

Answer = False
"""


while True:
    s1 = input("s1: ")
    if s1 == "exit":
        exit()
    s2 = input("s2: ")
    if s2 == "exit":
        exit()
    s1_list = list(s1)
    i = 1
    answer = False
    while i <= len(s1):
        s1_list.insert(len(s1), s1_list[0])
        s1_list.remove(s1_list[0])
        if (''.join(s1_list) == s2):
            answer = True
            break
        i += 1
    if answer:
        print("True")
    else:
        print("False")
