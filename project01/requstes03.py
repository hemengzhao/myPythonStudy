# 安装 requests
# pip install requests
import requests

url = "https://movie.douban.com/j/chart/top_list"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20,
}
resq = requests.get(url, params=param, headers=headers)
print(resq.json())
resq.close() # 关掉请求