import re

# # findall匹配字符串中所有的符合正则的内容
# lst = re.findall(r'\d+', '我的电话号是100876')
# print(lst)

# # finditer: 匹配字符串中所有的内容  返回的是迭代器, 从迭代器中拿到内容需要    .group()
# it = re.finditer(r'\d+', '我的电话号是100876, 我女朋友也的电话是：100432')
# for i in it:
#     print(i.group())

## search  找到一个结果就返回   返回的结果是match对象， 拿数据需要.group()
# s = re.search(r'\d+', '我的电话号是100876, 我女朋友也的电话是：100432')
# print(s.group())

## match 是从头开始匹配
# s = re.match(r'\d+', '我的电话号是100876, 我女朋友也的电话是：100432')
# print(s.group())

# # 预加载正则表达式
# obj = re.compile(r'\d+')
# ret = obj.finditer('我的电话号是100876, 我女朋友也的电话是：100432')
# print(ret)
# for i in ret:
#     print(i.group())

# ret = obj.findall('呵呵呵，我就不信你还我的100000元')
# print(ret)

#   (?P<分组名字>正则)  可以从正则中匹配的内容进一步提取内容
s = """
<div class='xyj'><span id='id1'>西游记</span></div>
<div class='hln'><span id='id12'>红楼梦</span></div>
<div class='shz'><span id='id2'>水浒传</span></div>
<div class='sgyy'><span id='id3'>三国演义</span></div>
"""

# re.S 让.能匹配换行符
obj = re.compile(r"<div class='(?P<id>.*?)'><span id='id\d+'>(?P<name>.*?)</span></div>", re.S)  
result = obj.finditer(s)
for i in result:
    print(i.group('name'))
    print(i.group('id'))