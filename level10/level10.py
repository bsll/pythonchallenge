#!/usr/bin/python
# -*- coding: utf-8 -*-
#按照惯例看源码
#基本上知道一个a = [1, 11, 21, 1211, 111221, 的序列
#所以答案就是构造这个序列，找出len(a[30])
#len(a[0]) len(a[1]) ....为1 2 2 4 6，所以猜一波斐波那契数列试试

def getLen(n):
    if n == 0:
        return 1;
    elif n == 1:
        return 2;
    elif n == 2:
        return 2;
    return getLen(n-1) + getLen(n-2)
#print(getLen(30))
#1664080,貌似并不是，看来还要从序列本身来推导
#百度一波，这个是外观队列。
#1，读法1个1，11，读法2个1，21，读法1个2，1个1，1211，读法1个1，1个2，2个1，111221，以此类推312211
#生成序列，是一个递推序列，生成规律，反复取重复元素的个数和重复元素，生成新序列

def readitem(item):
    allNum = list(item)
    count = 1
    count_item = allNum[0]
    result_item = []
    for i in range(1,len(allNum)):
        if allNum[i] == allNum[i-1]:
            count += 1
            count_item = allNum[i]
        else:
            result_item.append((str)(count))
            result_item.append((str)(count_item))
            count = 1
            count_item = allNum[i]
    result_item.append((str)(count))
    result_item.append((str)(count_item))
    return "".join(result_item)
item = "1";
n = 1
while n < 31:
   item = readitem(item)
   n = n + 1
print(len(list(item)))
#output:5808
#所以下一层连接为http://www.pythonchallenge.com/pc/return/5808.html
