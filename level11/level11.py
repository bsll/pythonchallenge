#!/usr/bin/python
# -*- coding: utf-8 -*-
#按照惯例看源码,图片名cave？title odd even ?
#尝试打印图片看看
from PIL import Image
im = Image.open('cave.jpg')
(width,height) = im.size
#print width,height
image1 = Image.new("RGB", (width, height), "#ffffff")
image2 = Image.new("RGB", (width, height), "#ffffff")
for h in range(0,height):
    for w in range(0,width):
            pixel = im.getpixel((w,h))
            if pixel[0] + pixel[1] + pixel[2] < 100:
                image1.putpixel((w,h),im.getpixel((w,h)))
            else:
                image2.putpixel((w,h),im.getpixel((w,h)))
#image1.show()
#image2.show()

#根据第二章图片打印的输出，可以看到evil
#所以下一层连接为http://www.pythonchallenge.com/pc/return/evil.html

#虽然解决问题但是并没有提现odd even,尝试这个思路
image1 = Image.new("RGB", (width/2, height/2))
image2 = Image.new("RGB", (width/2, height/2))
for h in range(0,height):
    for w in range(0,width):
            if(width + height)%2 == 0:
                image1.putpixel((w/2,h/2),im.getpixel((w,h)))
            else:
                image2.putpixel((w/2,h/2),im.getpixel((w,h)))
image1.show()
image2.show()
#同样可以看到evil
