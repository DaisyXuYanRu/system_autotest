from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager


# chrome driver 地址： https://registry.npmmirror.com/binary.html?path=chromedriver

class DriverConfig:
    def driver_config(self):
        """
        浏览器驱动
        :return:
        """
        options = webdriver.ChromeOptions()
        # 设置窗口大小，设置为1920*1080
        options.add_argument("window-size=1920,1080")
        # 去除"chrome正受到自动测试软件的控制"的提示
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # 解决selenium无法访问https的问题
        options.add_argument("--ignore-certificate-errors")
        # 允许忽略localhost上的TLS/SSL错误
        options.add_argument("--allow-insecure-localhost")
        # 设置为无痕模式
        options.add_argument("--incognito")
        # 设置为无头模式
        # options.add_argument("--headless")
        # 解决卡顿
        options.add_argument("--disable-gpu")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # 自动下载对应的浏览器驱动
        driver_path = ChromeDriverManager(url="https://mirrors.huaweicloud.com/chromedriver/",
                                          latest_release_url="https://mirrors.huaweicloud.com/chromedriver/LATEST_RELEASE",
                                          cache_manager=DriverCacheManager(valid_range=365)).install()
        # print("chrome驱动地址:", driver_path)
        driver = webdriver.Chrome(driver_path, options=options)
        # 删除所有cookies
        driver.delete_all_cookies()

        # 测试driver
        # driver.get("https://www.baidu.com/")
        # sleep(3)
        # driver.quit()

        return driver


if __name__ == '__main__':
    DriverConfig().driver_config()
