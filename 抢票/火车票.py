from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time



class LoginCart: 
     def check_element_exists(self, element_id):
        try:
            # 使用显式等待检查元素
            element = self.wait.until(
                EC.presence_of_element_located((By.ID, element_id))
            )
            print(f"找到元素: {element_id}")
            return True
        except:
            print(f"元素不存在: {element_id}")
            return False

     def __init__(self):
          # 初始化浏览器选项
        chrome_options = webdriver.ChromeOptions()
        # 添加一些选项来提高稳定性
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        # 初始化浏览器
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 20)  # 增加等待时间到20秒
        self.driver.maximize_window()  # 最大化窗口


     def open_login_page(self):
        self.driver.get("https://kyfw.12306.cn/otn/resources/login.html")
        time.sleep(2)
        # 输入账户密码
        try: 
             username_input = self.wait.until(
                    EC.presence_of_element_located((By.ID, "J-userName"))
                )
             print('username_input ===> ', username_input)
             username_input.clear()
             name = input()
             username_input.send_keys(name)
             print("输入用户名成功")
             time.sleep(2)
             
             password_input = self.wait.until(
                    EC.presence_of_element_located((By.ID, "J-password"))
                )
             password_input.clear()
             password = input()
             
             password_input.send_keys(password)
             print("输入用户名成功")
             time.sleep(2)

             login_btn = self.wait.until(
                    EC.element_to_be_clickable((By.ID, "J-login"))
                )
             login_btn.click()
             print("点击登录按钮成功")
             time.sleep(2)
             
             id_number = self.wait.until(EC.presence_of_element_located((By.ID, "id_card")))
             id_number.clear()
             id_number = input()
             id_number.send_keys(id_number)
             print("输入身份证号成功")
             time.sleep(2)
             
             
             code_input = self.wait.until(
                    EC.presence_of_element_located((By.ID, "code"))
                )
             code_input.clear()
             code = input()
             code_input.send_keys(code)
             print("输入验证码成功")
             time.sleep(2)

             btn = self.wait.until(
                    EC.element_to_be_clickable((By.ID, "sureClick"))
                )
             btn.click()
             print("点击验证码按钮成功")
             time.sleep(2)
             
             login_btn = self.wait.until(
                    EC.element_to_be_clickable((By.ID, "J-login"))
                )
             login_btn.click()
             print("点击登录按钮成功")
             time.sleep(2)

        except Exception as e:
            print(f"点击登录按钮失败: {str(e)}")
            return
        else:
            print("登录成功")
            is_login = True
            while is_login:
                if self.check_element_exists("J-index"):
                 print("点击首页按钮成功")
                 is_login = False
                else:
                    print("点击首页按钮失败")
                    time.sleep(2)

             



def main():
     print("hello")
     login_cart = LoginCart()
     login_cart.open_login_page()
     

if __name__ == "__main__":
    main()
