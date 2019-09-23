#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-09-23 23:43:18
# @Author  : Racterub (Racter Liu) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT

data = int(input("Input your time: "))

second = data % 60
second_trash = data // 60
minute = second_trash % 60
minute_trash = second_trash // 60
hour = minute_trash % 60
hour_trash = minute_trash // 60
day = hour_trash // 24

print("{} day(s), {} hour(s), {} minute(s) and {} second(s)".format(day, hour, minute, second))