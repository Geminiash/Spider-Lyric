import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class SimpleBrowserOpener:
    def __init__(self, driver_path, user_data_dir=None):
        self.driver_path = driver_path
        self.user_data_dir = user_data_dir  # 用户数据目录
        self.driver = None
    
    def setup_driver(self):
        """设置浏览器"""
        chrome_options = Options()
        
        # 基本设置
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
       

        # 添加用户数据目录以保持登录状态
        if self.user_data_dir:
            # 确保目录存在
            if not os.path.exists(self.user_data_dir):
                os.makedirs(self.user_data_dir)
                print(f"已创建用户数据目录: {self.user_data_dir}")
            
            chrome_options.add_argument(f'--user-data-dir={self.user_data_dir}')
            print(f"使用用户数据目录: {self.user_data_dir}")

        # 创建服务
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        return self.driver
    
    def open_url(self, url):
        """打开网页并保持"""
        try:
            # 打开网页
            print(f"正在打开网页: {url}")
            self.driver.get(url)
            time.sleep(3)
                    
            # 保持浏览器打开，直到用户关闭
            input("按Enter键关闭浏览器和程序...")
            
        except Exception as e:
            print(f"程序出错: {e}")
        finally:
            # 关闭浏览器
            if self.driver:
                self.driver.quit()
                print("浏览器已关闭")
                if self.user_data_dir:
                    print(f"登录信息已保存在: {self.user_data_dir}")

def main():
    
    # 配置参数
    driver_path = r"C:\Users\seren\AppData\Local\Programs\Python\Python311\chromedriver.exe"
    
    # 用户数据目录 - 使用 D:\work\cookies 目录
    user_data_dir = r"D:\work\cookies"
    # 不同网址，修改即可
    url = "https://www.douban.com/doulist/3936288/?start={start}&sort=time&playable=0&sub_type="
    
    print(f"Chrome驱动路径: {driver_path}")
    print(f"Cookies保存目录: {user_data_dir}")
    print(f"目标网址: {url}")
    print("=" * 60 + "\n")
    
    # 检查目录是否存在，如果不存在则创建
    if not os.path.exists(user_data_dir):
        print(f"目录 {user_data_dir} 不存在，正在创建...")
        os.makedirs(user_data_dir)
        print(f"目录创建成功！")
    
    # 创建浏览器实例
    opener = SimpleBrowserOpener(driver_path, user_data_dir)
    opener.setup_driver()
    opener.open_url(url)

if __name__ == "__main__":
    main()