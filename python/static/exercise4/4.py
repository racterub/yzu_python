#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-23 19:38:57
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

'''
我不知道老師是怎麼教質數判定的，如果老師有教，你也記得，就用老師的；如果老師有教你不記得，請去問別人；阿如果老師沒教，你也不知道要怎麼寫，就先把 code 看完，然後再去下面的連結稍微看一下

主要是因為我把 else 寫在 for loop 外面，可能有人會邏輯炸掉，所以附上解答。

中文:
https://note.pcwu.net/2017/02/26/python-loop-else/

英文:
https://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops
'''

data = int(input("Input the number you want to check if it is prime: "))

if data <= 1:
    print("Not a prime")
elif data == 2:
    print("Is a prime")
else:
    for i in range(2, data):
        print(data, i)
        if data % i == 0:
            print("Not a prime")
            break
    else:
        print("Is a prime")