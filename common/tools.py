import os

def get_project_path():
    """
    获取项目绝对路径
    :return:
    """
    # 项目名称 即是 文件夹的名称
    project_name = "system_autotest"
    # 获取当前的文件所在的文件夹路径 D:\PycharmProjects\py3.11.5\system_autotest\common
    file_path = os.path.dirname(__file__)
    # 截取项目路径 结果为 D:\PycharmProjects\py3.11.5\system_autotest
    return file_path[:file_path.find(project_name) + len(project_name)]


def sep(path, add_sep_before=False, add_sep_after=False):
    """
    拼接文件或者文件夹的路径，最后得到的路径前面或者后面增加/,因为windows和mac以及linux的路径分隔符不一样的，所以不能写死的，windows是 \ linux和mac是 /
    :param path: ["config", "environment.yaml"]
    :param add_sep_before: True
    :param add_sep_after:
    :return: \config\environment.yaml
    """
    # 把数组合并成路径 ["config", "environment.yaml"] => config\environment.yaml
    all_path = os.sep.join(path)
    # 前面增加路径分隔符
    if add_sep_before:
        all_path = os.sep + all_path
    # 后面面增加路径分隔符
    if add_sep_after:
        all_path = all_path + os.sep
    return all_path

if __name__ == '__main__':
    # print(get_project_path())
    print(sep(["config", "environment.yaml"], True))