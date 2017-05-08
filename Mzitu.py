# _*_ coding: utf-8 _*_
__author__ = 'FWJ'
__date__ = '17-5-8 下午2:47'

import requests
from bs4 import BeautifulSoup
import os

# 大部分网址必要，不然报错
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) "
                         "Chrome/22.0.1207.1 Safari/537.1"}
# 开始的url地址
all_url = 'http://www.mzitu.com/all'
start_html = requests.get(all_url, headers=headers)
# 请注意，concent 是二进制的数据，一般用于下载图片、视频、音频、等多媒体内容是才使用concent, 对于打印网页内容请使用text
print(start_html.text)


