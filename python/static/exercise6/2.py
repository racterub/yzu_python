#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-11-13 12:21:11
# @Author  : Racter Liu (racterub)
# @Mail    : racterub@gmail.com
# @Link    : https://racterub.io
# @License : MIT

def print_all_perfect_number():
    answer = []
    for i in range(1, 1001):
        factor = []
        for j in range(1, i):
            if (i % j) == 0:
                factor.append(j)
        if (sum(factor) == i):
            answer.append(i)
    return answer

print(print_all_perfect_number())
