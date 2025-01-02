# 安装 requests
# pip install requests
import requests

url = "https://fanyi.baidu.com/sug"
 
s = input('请输入你要翻译的英文单词')
data = {
    "kw": s
}
resq = requests.post(url, data=data)
print(resq.json())