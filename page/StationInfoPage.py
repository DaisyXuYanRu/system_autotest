from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.StationInfoBase import StationInfoBase


class StationInfoPage(StationInfoBase, ObjectMap):
    def station_info_dialog_input_value(self, driver, input_placeholder, input_value):
        """
        input输入
        :param driver:
        :param input_placeholder:
        :param input_value:
        :return:
        """
        input_xpath = self.station_info_input(input_placeholder,True)
        return self.element_fill_value(driver, By.XPATH, input_xpath, input_value)

    def click_Button(self, driver, button_name):
        """
        点击按钮
        :param driver:
        :param button_name:
        :return:
        """
        button_xpath = self.station_info_button(button_name)
        return self.element_click(driver, By.XPATH, button_xpath)

    def to_station_info(self,driver):
        self.element_to_url(driver, "/station/info")