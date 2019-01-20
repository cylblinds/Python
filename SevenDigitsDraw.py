#!/usr/bin/env python
# -*- coding:utf-8 -*-

import turtle
import time

def drawgap():
    turtle.penup()
    turtle.fd(5)

def drawline(draw): # 画线
    drawgap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawgap()
    turtle.right(90)

def drawdigit(digit): # 画数字
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,6,7,8,9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def drawdate(date): # 画日期数字,格式为'%Y-%M=%D+'
    turtle.pencolor('red')
    for i in date:
        if i == '-':
            turtle.write('年',font=('Arial',18,'normal'))
            turtle.pencolor('green')
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font=('Arial',18,'normal'))
            turtle.pencolor('blue')
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=('Arial',18,'normal'))
        else:
            drawdigit(eval(i))
    
def main():
    turtle.setup(1000,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    date = time.strftime('%Y-%m=%d+',time.gmtime()) # 获取当前时间，并按指定格式输出
    drawdate(date)
    turtle.hideturtle()
    turtle.done()

main()
