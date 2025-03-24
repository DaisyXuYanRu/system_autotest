from base.LoginBase import LoginBase
from base.ObjectMap import ObjectMap
from selenium.webdriver.common.by import By

from common.ocr_identify import OcrIdentify
from common.yaml_config import GetConf


class LoginPage(LoginBase, ObjectMap):
    def login_input_value(self, driver, input_placeholder, input_value):
        """
        登录页输入值
        :param driver:
        :param input_placeholder:
        :param input_value:
        :return:
        """
        input_xpath = self.login_input(input_placeholder)
        # return driver.find_element_by_xpath(input_xpath).send_keys(input_value)
        return self.element_fill_value(driver, By.XPATH, input_xpath, input_value)

    def click_login(self, driver, button_name):
        """
        点击登录
        :param driver:
        :param button_name:
        :return:
        """
        button_xpath = self.login_button(button_name)
        # return driver.find_element_by_xpath(button_xpath).click()
        return self.element_click(driver, By.XPATH, button_xpath)

    def login(self, driver, user):
        """
        登录
        :param driver: 浏览器驱动
        :param user: yaml文件中的user名称
        :return:
        """
        self.element_to_url(driver, "/login")
        username, password = GetConf().get_username_password(user)
        self.login_input_value(driver, "请输入账号", username)
        self.login_input_value(driver, "请输入密码", password)
        # 图片验证码处理
        captcha_xpath = self.captcha()
        ele_img_path = self.element_screenshot(driver, By.XPATH, captcha_xpath)
        identify = OcrIdentify().identify(ele_img_path)
        # print("验证码:", identify)
        input_captcha_xpath = self.input_captcha()
        self.element_fill_value(driver, By.XPATH, input_captcha_xpath, identify)
        self.click_login(driver, "登录")
