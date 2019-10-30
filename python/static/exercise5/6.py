#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-29 20:34:20
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

'''
一個字一個字看，如果是英文字，先存進 tmp ，如果遇到空白，將 tmp 裡面的字串反轉丟去 answer，把 tmp 清空，然後在 answer 加上空白，持續這樣之後，如果最後一個字不是空白，會導致 tmp 裡面的內容沒有存進 answer 裡面，所以 for loop 後再加上 tmp 的內容
'''




string = input("Input your string: ") #測資: Hello World

answer = ''
tmp = ''
for i in range(len(string)):
    if string[i] != ' ':
        tmp += string[i]
    else:
        #Reverse string
        answer += tmp[::-1]
        tmp = ''
        answer += ' '

answer += tmp


print(answer)
#輸出: olleH World