#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-12-12 11:11:39
# @Author  : Racter Liu (racterub) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT

import csv


def getMonth(n):
    return int(n.strip().split("/")[1])


def listCreate(n):
    res = []
    for i in range(n):
        res.append(list())
    return res


result = listCreate(12)

f = open("b_10co2008CO_err.txt")
data = f.readlines()[1:] #去掉標頭

for i in data:
    queue = i.strip().split('\t')
    if (len(queue) == 3):
        month = getMonth(queue[0])
        try:
            close = float(queue[2])
        except ValueError:
            continue
        result[month-1].append(close)

print("Month    max    min    average")
for i in range(len(result)):
    print("{:<9d}{:<7.1f}{:<7.1f}{:<.1f}".format(i+1, max(result[i]), min(result[i]), (sum(result[i])/len(result[i]))))

f.close()
f = open("out.csv", "w")
writer = csv.writer(f)
writer.writerow(["Month", "max", "min", "average"])
for i in range(len(result)):
    writer.writerow([i+1, max(result[i]), min(result[i]), round(sum(result[i])/len(result[i]), 2)])
