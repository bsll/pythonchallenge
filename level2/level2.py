#!/usr/bin/python
# -*- coding: utf-8 -*-

#根据提示显然是要查看网页源代码,然后根据提示是要从一大串字符串里找到所有只出现一次的字符。
#字符串文件存储到data

string = ""
f = file('level2_data')
for line in f:
    for i in range(0,len(line.strip())):
        if line[i].isalpha():
            string += line[i]

print string
f.close()

#output:equality
#下一级网址:http://www.pythonchallenge.com/pc/def/equality.html
