from time import sleep

from config.driver_config import DriverConfig
from selenium.webdriver.common.by import By

driver = DriverConfig().driver_config()
driver.get("https://yunwei.zgyun.link/#/login")
sleep(8)
driver.find_element_by_xpath("//input[@placeholder='请输入账号']").send_keys("test")
sleep(1)
driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys("test")
sleep(1)
driver.find_element_by_xpath("//span[text()='登录']/parent::button").click()