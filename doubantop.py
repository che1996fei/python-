from lxml import etree
import requests
import csv

fp = open('C://Users/FLY/Desktop/doubanbook.csv', 'wt', newline='', encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('name', 'url', 'author', 'publisher', 'data', 'price', 'rate', 'comment'))

urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0, 250, 25)]

for url in urls:
    html = requests.get(url)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//tr[@class="item"]')
    for info in infos:
        name = info.xpath('td/div/a/@title')[0]
        url = info.xpath('td/div/a/@href')[0]
        book_infos = info.xpath('td/p/text()')[0]
        author = book_infos.split('/')[0]
        publisher = book_infos.split('/')[-3]
        data = book_infos.split('/')[-2]
        price = book_infos.split('/')[-1]
        rate = info.xpath('td/div/span[2]/text()')[0]
        comments = info.xpath('td/p/span/text')
        comment = comments[0] if len(comments) != 0 else "空"
        writer.writerow((name, url, author, publisher, data, price, rate, comment))

fp.close()
