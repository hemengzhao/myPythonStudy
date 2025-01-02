from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 安装必要的库
# pip install selenium
# pip install webdriver_manager
class BaiduLogin:
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

    def login(self, username, password):
        try:
            # 打开百度首页
            self.driver.get("https://www.baidu.com")
            time.sleep(2)  # 等待页面完全加载
            
            # 点击登录按钮
            try:
                login_btn = self.wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "#s-top-loginbtn"))
                )
                print("找到登录按钮")
                login_btn.click()
                print("点击登录按钮成功")
            except Exception as e:
                print(f"点击登录按钮失败: {str(e)}")
                return
            
            # 等待登录框出现并切换
            # try:
            #     time.sleep(2)  # 给页面一些时间来加载iframe
            #     login_frame = self.wait.until(
            #         EC.presence_of_element_located((By.ID, "passport-login-pop-dialog"))
            #     )
            #     self.driver.switch_to.frame(login_frame)
            #     print("成功切换到登录框")
            # except Exception as e:
            #     print(f"切换到登录框失败: {str(e)}")
            #     return
            
            # 确保在用户名登录模式
            try:
                username_login_btn = self.wait.until(
                    EC.presence_of_element_located((By.ID, "TANGRAM__PSP_11__changePwdCodeItem"))
                )
                username_login_btn.click()
                print("切换到用户名登录模式")
            except Exception as e:
                print("已经是用户名登录模式或切换失败")
            
            # 输入用户名和密码
            try:
                username_input = self.wait.until(
                    EC.presence_of_element_located((By.ID, "TANGRAM__PSP_11__userName"))
                )
                username_input.clear()
                username_input.send_keys(username)
                print("输入用户名成功")
                
                password_input = self.wait.until(
                    EC.presence_of_element_located((By.ID, "TANGRAM__PSP_11__password"))
                )
                password_input.clear()
                password_input.send_keys(password)
                print("输入密码成功")
                
                i_read = self.wait.until(
                    EC.presence_of_element_located((By.ID, "TANGRAM__PSP_11__isAgree"))
                )
                i_read.click() 
                print("同意协议")

                # 点击登录按钮
                submit_btn = self.wait.until(
                    EC.element_to_be_clickable((By.ID, "TANGRAM__PSP_11__submit"))
                )
                submit_btn.click()
                print("点击提交按钮成功")
                
                # 等待登录成功
                time.sleep(5)
                print("登录流程完成")
                
            except Exception as e:
                print(f"输入信息或提交过程中出错: {str(e)}")
                
        except Exception as e:
            print(f"登录过程中出现错误: {str(e)}")
        finally:
            # 切回主框架
            try:
                self.driver.switch_to.default_content()
            except:
                pass
        
    def close(self):
        try:
            self.driver.quit()
            print("浏览器已关闭")
        except Exception as e:
            print(f"关闭浏览器时出错: {str(e)}")

def main():
    baidu = BaiduLogin()
    
    # 设置你的百度账号和密码
    username = "你的用户名"
    password = "你的密码"
    
    try:
        baidu.login(username, password)
        time.sleep(5)  # 登录后等待一段时间
    finally:
        baidu.close()

if __name__ == "__main__":
    main()
