from time import sleep

from config.driver_config import DriverConfig
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage
from page.StationInfoPage import StationInfoPage


class TestStation:
    def test_station_info(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'admin')
        sleep(3)
        LeftMenuPage().click_level_one_menu(driver,'场站管理')
        sleep(0.1)
        LeftMenuPage().click_level_two_menu(driver, '场站信息管理')
        sleep(1)
        StationInfoPage().click_Button(driver,' 新建 ')
        sleep(0.1)
        StationInfoPage().station_info_dialog_input_value(driver,'请输入场站名称','草泥马')
        sleep(3)
        driver.quit()
