#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-11-25 23:58:55
# @Author  : Racter Liu (racterub) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT

import csv

f = open("./Dengue_Daily_EN.csv")
rows = csv.DictReader(f)

#1
scope = ["Taipei City", "New Taipei City"]
for row in rows:
    if row["County_living"] in scope:
        print("Date_Onset: {}, Sex: {}, Age_Group: {}, County_living: {}, Township_living: {}".format(row["Date_Onset"], row["Sex"], row["Age_Group"], row["County_living"], row["Township_living"]))

#2
def dataSplitter(data):
    return data.split("/")

def createList(n):
    data = []
    for i in range(n):
        tmp = []
        for j in range(12):
            tmp.append(0)
        data.append(tmp)
    return data

casesDate = createList(22) #Create lists to store result

f = open("./Dengue_Daily_EN.csv")
rows = csv.DictReader(f)
for row in rows:
    year, month, day = dataSplitter(row["Date_Onset"])
    casesDate[int(year)-1998][int(month)-1] += 1

for i in range(len(casesDate)):
    for k in range(len(casesDate[0])):
        print("{}/{} cases: {}".format(i + 1998, k+1, casesDate[i][k]))
