# 安装 requests
# pip install requests
import requests

url = "https://www.sogou.com/web?query=%E5%91%A8%E6%9D%B0%E4%BC%A6"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
resq = requests.get(url, headers=headers)
print(resq.text)