#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-10-15 23:33:03
# @Author  : Racterub (Racter Liu) (racterub@gmail.com)
# @Link    : https://racterub.io
# @License : MIT

data = int(input("Input your range:")) #測資 500

answer = []
for i in range(1, data+1):
    factor = []
    for j in range(1, i):
        if i % j == 0:
            factor.append(j)
    if sum(factor) == i:
        answer.append(str(i))

print("Answer: ", ', '.join(answer))
#輸出: Answer:  6, 28, 496