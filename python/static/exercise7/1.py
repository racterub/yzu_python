#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-11-18 23:46:31
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

f = open("golf.txt", "w")

count = int(input("How many players: "))

for _ in range(count):
    name = input("Name: ")
    score = input("Score: ")
    f.write(name + '\n')
    f.write(score + '\n')