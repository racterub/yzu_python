#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-09-08 23:16:59
# @Author  : Racterub (Racter Liu) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT

male = int(input("Enter number of males: "))
female = int(input("Enter number of females: "))

total = male + female
percent_male = round((male/total)*100)
percent_female = round((female/total)*100)

print("Percent of males: ", percent_male, "%")
print("Percent of females: ", percent_female, "%")