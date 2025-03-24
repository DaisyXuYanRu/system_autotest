from config.driver_config import DriverConfig
from time import sleep

from page.LoginPage import LoginPage


class TestLogin:
    def test_login(self):
        driver = DriverConfig().driver_config()
        # driver.get("https://yunwei.zgyun.link/#/login")
        # sleep(3)
        # LoginPage().login_input_value(driver, "请输入账号", "test")
        # sleep(1)
        # LoginPage().login_input_value(driver,"请输入密码","test")
        # sleep(1)
        # LoginPage().click_login(driver,"登录")
        LoginPage().login(driver,'admin')
        sleep(3)
        driver.quit()

