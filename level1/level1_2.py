#!/usr/bin/python
# -*- coding: utf-8 -*-
from string import maketrans   # 调用 maketrans 函数。
from string import translate
#maketrans完成映射
#translate使用映射关系进行替换

intab = "abcdefghijklmnopqrstuvwsyz"
outtab = "cdefghijklmnopqrstuvwsyzab"
trantab = maketrans(intab, outtab)
#http://www.pythonchallenge.com/pc/def/map.html
string = "map"
print translate(string,trantab)


#output:ocr
#所以下一级的网址为 http://www.pythonchallenge.com/pc/def/ocr.html
