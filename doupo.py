import requests
import re

f = open('C:/Users/FLY/Desktop/doupo2.txt', 'a+', encoding='utf-8')


urls = ['https://m.doupocangqiong1.com/1/{}.html'.format(str(i)) for i in range(1921, 1922)]
for url in urls:
    res = requests.get(url)
    title = re.findall('<h1 class="title">(.*)</h1>', res.content.decode('utf-8'), re.S)[0]
    contents = re.findall('<div id="articlecon" class="articlecon"><p>(.*)</p></div>', res.content.decode('utf-8'),
                          re.S)
    contentsss = re.compile(r'<[^>]+>', re.S)
    result = contentsss.sub('', ';'.join(contents))
    f.write(title + '\n\n')
    f.write(result + '\n\n')



