#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-29 19:41:03
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

'''
email 格式: username + @ + 網站名稱
先檢查最後面是不是 .yzu.edu.tw
然後看一下有在 yzu 前面有沒有其他子網域 e.x. mail.yzu.edu.tw (mail 就是子域名)
'''

email = input("Input your email address: ")

#Check domain
if email[-11:] == ".yzu.edu.tw":
    domain = email.split('@')[1].split('.')
    if len(domain) == 4:
        print("Valid Email")
        exit()
    else:
        print("Invalid Email")
else:
    print("Invalid Email")
