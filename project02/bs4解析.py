# bs4 安装
# pip install bs4 

import requests
from bs4 import BeautifulSoup
url='http://www.xinfadi.com.cn/priceDetail.html'
resq =requests.get(url)


page = BeautifulSoup(resq.text, 'html.parser')

# 从bs4查找数据
# find
# find_all

table = page.find('table', attrs={"border": '0'})
print(table)