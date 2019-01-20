#!/usr/bin/env python
# -*- coding:utf-8 -*-

count = 0
def hanoi(n,src,dst,mid):
    global count
    if n == 1:
        print('{}:{}->{}'.format(1,src,dst))
        count = count+1
    else:
        hanoi(n-1,src,mid,dst)
        print('{}:{}->{}'.format(n,src,dst))
        count = count+1
        hanoi(n-1,mid,dst,src)

n = input()
hanoi(eval(n),'A','C','B')
print(count)
