#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-11-26 00:32:09
# @Author  : Racter Liu (racterub) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT


f = open("10co2008CO_err.txt")
import pprint
data = f.readlines()
head = data[0]
data = data[1:]
data = [i.strip().split('\t') for i in data]


def init_list_of_objects(size):
    list_of_objects = list()
    for i in range(0,size):
        list_of_objects.append( list() ) #different object reference each time
    return list_of_objects


result = init_list_of_objects(12)


def monthSpitter(data):
    return data.split('/')[1]

for i in range(len(data)):
    month = int(monthSpitter(data[i][0]))
    try:
        tmp = data[i][2]
        try:
            tmp = float(tmp)
            result[month-1].append(tmp)
        except ValueError:
            pass
    except IndexError:
        pass

print("{:6s}   {:6s}   {:6s}".format("Month", "max", "min"))
for i in range(len(result)):
    print("{:<6d}   {:>.2f}   {:.2f}".format(i, max(result[i]), min(result[i]))