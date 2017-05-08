# _*_ coding: utf-8 _*_
__author__ = 'FWJ'
__date__ = '17-5-8 下午2:47'

import requests
from bs4 import BeautifulSoup
import os
import time


start = time.clock()


# 大部分网址必要，不然报错
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) "
                         "Chrome/22.0.1207.1 Safari/537.1"}
# 开始的url地址
all_url = 'http://www.mzitu.com/all'
# 使用requests中get方法
start_html = requests.get(all_url, headers=headers)
# 请注意,concent是二进制的数据,一般用于下载图片,视频,音频,等多媒体内容是才使用concent,对于打印网页内容请使用text
# print(start_html.text)
# 使用beautifulsoup解析
Soup = BeautifulSoup(start_html.text, 'lxml')
# find_all是查找指定网页内的所有标签,返回是一个列表,而find只查找给定的标签一次
li_list = Soup.find('div', class_='all').find_all('a')
for li in li_list:
    pass
    title = li.get_text()
    path = str(title).strip()

    # 添加文件
    os.makedirs(os.path.join("/home/fwj/mzitu", path))
    os.chdir("/home/fwj/mzitu/" + path)

    # 取出标签的文本
    # print(title)
    href = li['href']
    print(title, href)
    # 获取href内容
    html = requests.get(href, headers=headers)
    html_soup = BeautifulSoup(html.text, 'lxml')
    # 获取span标签的text内容
    max_span = html_soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
    for page in range(1, int(max_span)+1):
        page_url = href + '/' + str(page)
        # print(page_url)
        img_html = requests.get(page_url, headers=headers)
        print(img_html)
        img_soup = BeautifulSoup(img_html.text, 'lxml')
        img_url = img_soup.find('div', class_='main-image').find('img')['src']
        # print(img_url)
        name = img_url[-9:-4]
        img = requests.get(img_url, headers=headers)
        f = open(name+'.jpg', 'ab')
        f.write(img.content)
        f.close()
end = time.clock()
print("read: %f s" % (end - start))



