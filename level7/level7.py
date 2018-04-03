#!/usr/bin/python
# -*- coding: utf-8 -*-
#看样子图片藏了东西，先下载图片
#破解思路：先找到打马赛克的那一段图片，打印出像素值
from PIL import Image
im = Image.open('oxygen.png')
(width,height) = im.size
for h in range(0,height):
    pixel = im.getpixel((0,h))
    if(pixel[0] == pixel[1] and pixel[0] == pixel[2]):
        print h,
print "\n"
#output:43 44 45 46 47 48 49 50 51 95
#打印43到51的像素值转换成的ASCII
#数据重复，所以只打印一行
for w in range(0,width):
    pixel = im.getpixel((w,43))
    if(pixel[0] == pixel[1] and pixel[0] == pixel[2]):
        print chr(pixel[0]),
#输出字符串有很多重复，去重操作
print "\n"
res = ""
for w in range(0,width):
    pixel = im.getpixel((w,43))
    if(pixel[0] == pixel[1] and pixel[0] == pixel[2]):
        res = res + chr(pixel[0])
print res
#output:smart guy, you made it. the next level is [105, 10, 16, 101, 103, 14, 105, 16, 121]
#明显不能全部转换成ascii,重新对最后一行去重
i = 0
res = ""
for w in range(0,width):
    pixel = im.getpixel((w,43))
    if(pixel[0] == pixel[1] and pixel[0] == pixel[2]):
        if(i%7 == 0):
            res = res + chr(pixel[0])
        i += 1
print res
res_list = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for i in res_list:
    print chr(i),
#output:smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
#i n t e g r i t y
#下一级url:http://www.pythonchallenge.com/pc/def/integrity.html
