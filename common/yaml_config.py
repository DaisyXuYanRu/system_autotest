# 需要安装 pyyaml
import yaml
# 引入工具函数
from common.tools import get_project_path, sep


class GetConf:
    # GetConf() 相当于执行这个函数，读取environment.yaml配置文件的内容
    def __init__(self):
        # 找到environment.yaml文件并以读取的方式打开，encoding="utf-8"，utf-8编码格式，编程都是用这个格式打开文件，防止乱码
        with open(get_project_path() + sep(["config", "environment.yaml"], add_sep_before=True), "r",
                  encoding="utf-8") as env_file:
            # 读取整个文件的内容赋值给 self.env ，一般是一个dict
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)
            # print(self.env)

    def get_username_password(self, user):
        return self.env["user"][user]["username"], self.env["user"][user]["password"]

    def get_url(self):
        return self.env["url"]


if __name__ == '__main__':
    print(GetConf())
