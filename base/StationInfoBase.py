class StationInfoBase:

    def station_info_input(self, input_placeholder, is_dialog=False):
        """
        input输入
        :param input_placeholder:
        :return:
        """
        if is_dialog:
            return "//div[@class='el-dialog']//input[@placeholder='" + input_placeholder + "']"
        else:
            return "//input[@placeholder='" + input_placeholder + "']"

    def station_info_button(self, button_name):
        """
        按钮
        :param button_name:
        :return:
        """
        return "//span[text()='" + button_name + "']/parent::button"
