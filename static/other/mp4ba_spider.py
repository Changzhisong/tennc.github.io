#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author: tennc
# date: 2015/9/10
# filename: mp4ba_spider.py
# 
# The MIT License
# 
# Copyright (c) 2015
# 
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.


import requests
from bs4 import BeautifulSoup
import time
import re

pchinese=re.compile('([\u4e00-\u9fa5]+)+?') #匹配中文 匹配电影类型
mingzitemp=re.compile('(target="_blank">(\s+)).(.+)') #moive name
urltemp = re.compile('(hash=)(\S+)')#匹配hash
file = open('mp4ba.txt','w',encoding="utf-8")
for i in range(1,68):
    response = requests.get("http://www.mp4ba.com/index.php?page=" + str(i))
    soup = BeautifulSoup(response.text,"html.parser")
    a = soup.find("tbody").findAll('tr')
    for m in a :
        #print(m)
        mingzi = str(mingzitemp.findall(str(m))).split()[-1].replace("</a>')]","").replace("'","").replace('</a>")]',"").replace('"',"")
        leixing = str(pchinese.findall(str(m))[0])
        urldown = str(urltemp.findall(str(m))[:][-1]).replace("'hash=', '","magnet:?xt=urn:btih:").replace("'","").replace('"',"").replace("(","").replace(')','')
        #print(urldown)
        data = str(leixing) + "," + str(mingzi) + "," + str(urldown) + "\n"
        file.write(data)
    time.sleep(2) #延时1秒后继续运行下一页

file.close()
