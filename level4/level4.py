#!/usr/bin/python
# -*- coding: utf-8 -*-
#根据提示像是要使用urllib,然后从结果解析
#点击图片可以看到加了一个nothing=12345的参数，然后又跳转到next nothing=44827
#同时根据网页源码显示，跳转400次就够了，所以用循环反复读取分析链接即可。

import urllib2
import urllib

value = 12345
i = 0
while(i < 400 ):
    #从浏览器取header属性构造请求头
    req = urllib2.Request('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + (str)(value))
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36')
    req.add_header('Cookie','info=you+should+have+followed+busynothing...')
    req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')
    req.add_header('Accept-Encoding','gzip, deflate')
    req.add_header('Accept-Language','zh-CN,zh;q=0.9,en;q=0.8')
    req.add_header('Cache-Control','max-age=0')
    req.add_header('Connection','keep-alive')
    req.add_header('Upgrade-Insecure-Requests',1)
    response =  urllib2.urlopen(req)
    result = response.read()
    #print result
    #根据打印的结果，当result为html为后缀的时候终止循环
    if(result.endswith('html')):
         print result
         break
    line = result.split(" ")
    value = line[len(line)-1]
    i += 1


#output:peak.html
#url:http://www.pythonchallenge.com/pc/def/peak.html
