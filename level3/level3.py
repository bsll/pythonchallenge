#!/usr/bin/python
# -*- coding: utf-8 -*-
#根据提示要找的是每个周围严格有三个大写字母的小写字母。eg:ABCdEFG
#思路把整个文件拼起来，然后利用正则查找
import re
f = file('level3_data')
string = ''
for line in f:
    line = line.strip()
    string = string + line
#因为为严格，所以前后用小写作为标志
pattern = re.compile(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]')
result = pattern.findall(string)
print "".join(result)

#output:linkedlist
#url:http://www.pythonchallenge.com/pc/def/linkedlist.html
