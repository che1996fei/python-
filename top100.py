# coding=utf-8

import re
import urllib.request
top_urls = []
top_num = 1
url = "https://movie.douban.com/top250?start="
for num in range(4):
    top_urls.append(url + str(num * 25))


for i in top_urls:
    html = urllib.request.urlopen(i).read().decode('utf-8')
    top_tag = re.compile(r'<span class="title">(.*)</span>')
    title = re.findall(top_tag, html)
    print(title)
    for i in title:
         if i.find('/') == -1:
            print('Top' + str(top_num) + '  ' + i)
            top_num += 1
