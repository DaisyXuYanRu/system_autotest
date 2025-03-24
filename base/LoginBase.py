
class LoginBase:

    def login_input(self, input_placeholder):
        """
        登录用户名、密码输入框
        :param input_placeholder:
        :return:
        """
        return "//input[@placeholder='" + input_placeholder + "']"

    def login_button(self, button_name):
        """
        登录按钮
        :param button_name:
        :return:
        """
        return "//span[text()='" + button_name + "']/parent::button"

    def captcha(self):
        """
        验证码
        :return:
        """
        return "//img[@alt='验证码']"

    def input_captcha(self):
        """
        输入验证码的输入框
        :return:
        """
        return "//input[@placeholder='请输入验证码']"