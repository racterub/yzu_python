#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-29 19:25:36
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

'''
IP 用點來分有四個部分，分別是 A class, B class, C class, D class,
A class 和 B class 指定要為 140.138
C class 和 D class 指定要 0 <= number <= 255
'''


ip = input("Input your IP: ")


#IP has 4 classes A.B.C.D
ip_segment = ip.split('.')

#Check if ip has 4 segments
if (len(ip_segment) != 4):
    print("Invalid IP")
    exit()

#Unpack ip segments
aclass, bclass, cclass, dclass = ip_segment
#Check a_class and b_class is 140.138
if (aclass != '140' or bclass != '138'):
    print("Invalid IP")
    exit()
#Check c_class and b_class integer range
if (0 <= int(cclass) <= 255 and 0 <= int(dclass) <= 255):
    print("Valid IP")
    exit()
else:
    print("Invalid IP")
    exit()