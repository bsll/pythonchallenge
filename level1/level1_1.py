#!/usr/bin/python
# -*- coding: utf-8 -*-

#根据屏幕提示做两位的移位转换
string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
result_string = ""
#ord获取字符对应的ascii编码，chr将ascii编码改成字符
for i in range(0,len(string)):
    if ord(string[i]) >= ord('a') and ord(string[i]) <= ord('x'):
        result_string += chr(ord(string[i]) + 2)
    elif ord(string[i]) >= ord('y') and ord(string[i]) <= ord('z'):
        result_string += chr(ord(string[i]) + 2-26)
    else:
        result_string += string[i]
print result_string


#输出的提示为：
#i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
#对应提示要思考两遍，使用string.maketrans(),具体见level1_2.py
