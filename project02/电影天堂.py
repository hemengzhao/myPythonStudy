# 定位到2024比看片
# 从2024比看片中提取自页面地址
# 请求子页面，拿到我们想要下载的地址
import requests 
import re
domain = 'https://www.dytt89.com/'
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

# verify=False 去电安全验证
resq = requests.get(domain, verify=False, headers=headers) 
resq.encoding= 'gb2312'
page_content = resq.text

child_href_list = []

obj1 = re.compile(r'2024新片精品.*?<ul>(?P<ul>.*?)</ul>', re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名(?P<move>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<down>.*?)">', re.S)

resutlt = obj1.finditer(page_content)
ul=next(resutlt).group('ul')

# print(ul)
# 或者下面写法
# for it in resutlt:
#     ul= it.group('ul')
#     print(ul)
#     resutlt1 = obj2.finditer(ul)
#     for itt in resutlt1:
#         href= itt.group('href')
#         child_href = domain + href.strip('/')
#         print(child_href)


resutlt1 = obj2.finditer(ul)
for itt in resutlt1:
    href= itt.group('href')
    child_href = domain + href.strip('/') 
    child_href_list.append(child_href)
 

# 提取自页面内容
for href in child_href_list:
    child_resq = requests.get(href, verify=False, headers=headers) 
    child_resq.encoding= 'gb2312' 
    reslte3 = obj3.search(child_resq.text) 
    print(reslte3.group('move'))
    print(reslte3.group('down'))
    break
 