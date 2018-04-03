#!/usr/bin/python
# -*- coding: utf-8 -*-
#根据提示，把网页的html后缀改成zip即可以下在数据文件，解压到channel
#根据readme提示从90052开始找数据，下一个是94191，，看上去可以循环打开文件看看
#给出collect the comments. 的提示。试着利用python打开zip文件的注释。
#原来zip文件注释有两种方式一种是zip包的注释，一种是子文件的注释
#zip包没有注释，子文件有注释可以拼成答案
#打印出子文件的注释得到字母形状的HOCKEY
#打开网址http://www.pythonchallenge.com/pc/def/hookey.html，提示it's in the air. look at the letters.
#字母分别为oxygen
#所以最终网址为http://www.pythonchallenge.com/pc/def/oxygen.html
filenum = '90052'
num_dict = {}
ss = ""
while True:
    f = open("./channel/" + (filenum) + ".txt","r")
    line = f.readline().strip().split()
    filenum = line[len(line)-1]
    if(filenum.isdigit() == False):
        #print line
        break

import zipfile
filenum = '90052'
zf = zipfile.ZipFile('channel.zip','r')
ss = ''
while True:
    ss += zf.getinfo(filenum+".txt").comment.decode('utf-8')
    line = zf.read(filenum+".txt").strip().split()
    filenum = line[len(line)-1]
    if(filenum.isdigit() == False):
        break
print ss

'''
output:
****************************************************************
****************************************************************
**                                                            **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
**                                                            **
****************************************************************
 **************************************************************
url:http://www.pythonchallenge.com/pc/def/hookey.html
it's in the air. look at the letters.
url:http://www.pythonchallenge.com/pc/def/oxygen.html
'''
