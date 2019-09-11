"""
PO 文件的基类  修改文件内容 测试pycharm的提交
"""
from C_WebAutoTestTPshop.utils import DriverUtil


class BasePage(object):
    """对象库层-基类"""

    def __init__(self):
        self.driver = DriverUtil.get_driver()  # 获取浏览器对象

    def find_element_func(self, location):
        """元素定位方法"""
        return self.driver.find_element(location[0], location[1])


class BaseHandle(object):
    """操作层-基类"""

    @staticmethod
    def input_text(element, text):
        """
        输入文本方法
        :param element: 元素对象
        :param text: 要输入的文本内容
        :return: 无返回值
        """
        element.clear()
        element.send_keys(text)

    @staticmethod
    def click_element(element):
        """
        点击元素方法
        :param element: 目标元素
        :return: 无返回值
        """
        element.click()

    @staticmethod
    def get_element_text(element):
        """
        返回元素的文本内容
        :param element: 元素对象
        :return: 文本内容
        """
        return element.text
