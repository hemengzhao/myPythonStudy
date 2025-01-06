from flask import Flask, request
import requests
from urllib.parse import urljoin
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# 目标服务器地址
TARGET_URL = "https://api.example.com"  # 替换为你要代理的目标服务器

class ReverseProxy:
    def __init__(self, target_url):
        self.target_url = target_url

    def proxy_request(self):
        """处理代理请求"""
        try:
            # 构建目标URL
            path = request.path
            target_url = urljoin(self.target_url, path)
            
            # 获取原始请求的headers
            headers = {key: value for key, value in request.headers if key.lower() != 'host'}
            
            # 获取查询参数
            params = request.args.to_dict()
            
            # 获取请求体
            data = request.get_data()
            
            # 发送请求到目标服务器
            response = requests.request(
                method=request.method,
                url=target_url,
                headers=headers,
                params=params,
                data=data,
                stream=True,
                verify=False  # 如果目标使用自签名证书，可以设置为False
            )
            
            # 记录请求信息
            logger.info(f"Proxied request: {request.method} {target_url}")
            logger.info(f"Status code: {response.status_code}")
            
            # 返回响应
            return (
                response.content,
                response.status_code,
                dict(response.headers)
            )
            
        except requests.RequestException as e:
            logger.error(f"Proxy error: {str(e)}")
            return f"Proxy error: {str(e)}", 500

# 创建代理实例
proxy = ReverseProxy(TARGET_URL)

# 处理所有请求方法
@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def proxy_all(path):
    return proxy.proxy_request()

def main():
    # 配置服务器
    app.config['JSON_AS_ASCII'] = False
    
    # 启动服务器
    app.run(
        host='0.0.0.0',  # 监听所有网络接口
        port=5000,       # 监听端口
        debug=True       # 开发模式，生产环境应设为False
    )

if __name__ == '__main__':
    main()
