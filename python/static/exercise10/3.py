#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-12-12 10:28:51
# @Author  : Racter Liu (racterub) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT

import csv

#建立空 list
def listCreate(n):
    data = []
    for i in range(n):
        data.append([0])
    return data

#從 2012/01/22 格式中取出年份
def getYear(n):
    return int(n.strip().split("/")[0])

file = open("./a_Dengue_Daily_EN.csv")
reader = csv.DictReader(file)

result = listCreate(20) #拿來儲存答案

for row in reader:
    if row["County_living"] == "Kaohsiung City":
        year = getYear(row["Date_Onset"])
        result[year-2000][0] += 1

print("Year    num_cases")
for i in range(len(result)):
    print("{:<8d}{:<d}".format(i+2000, result[i][0]))


file.close()
file = open("out.csv", "w")
writer = csv.writer(file)
writer.writerow(["Year", "num_cases"])
for i in range(len(result)):
    writer.writerow([i+2000, result[i][0]])