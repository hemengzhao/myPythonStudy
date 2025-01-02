# 拿到页面源码 
# 解析
import requests
import re
import csv

url='https://movie.douban.com/top250'
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
resq = requests.get(url, headers=headers)
page_content = resq.text

# 解析数据
object = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">'
                    r'.*?<br>(?P<year>.*?)&nbsp;.*?<span class="rating_num" property="v:average">(?P<fen>.*?)</span>'
                    r'.*?<span>(?P<total>\d*?)人评价</span>', re.S)

list = object.finditer(page_content)
f = open('data.csv', mode='w')
csvWriter = csv.writer(f)
for item in list:
    # print(item.group('name'))
    # print(item.group('year').strip())
    # print(item.group('fen'))
    # print(item.group('total'))
    dic=item.groupdict()
    dic['year'] = dic['year'].strip()
    csvWriter.writerow(dic.values()) 
f.close()
print('over!')

