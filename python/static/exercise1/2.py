#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-09-23 23:43:18
# @Author  : Racterub (Racter Liu) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT

data = int(input("Input your time: ")) #測資: 3667

second = data % 60
second_trash = data // 60
minute = second_trash % 60
minute_trash = second_trash // 60
hour = minute_trash % 60
hour_trash = minute_trash // 60
day = hour_trash // 24

print(day, "day(s),", hour, "hour(s),", minute, "minute(s) and", second, "second(s)")
#輸出: 0 day(s), 1 hour(s), 1 minute(s) and 7 second(s)