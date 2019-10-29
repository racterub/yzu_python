#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-29 19:41:03
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

email = input("Input your email address: ")

#Check domain
if email[-11:] != ".yzu.edu.tw":
    print("Invalid Email")
    exit()

#Check domain if it has four level domain
domain = email.split('@')[1].split('.')
if len(domain) != 4:
    print("Invalid Email")
    exit()


print("Valid Email")
