"""
测试用例   登录功能
"""
import json
import logging
import sys
import time
import unittest

from parameterized import parameterized

from C_WebAutoTestTPshop.base import *
from C_WebAutoTestTPshop.page.index_page import IndexProxy
from C_WebAutoTestTPshop.page.login_page import LoginProxy
from C_WebAutoTestTPshop.utils import DriverUtil


def read_json():
    with open(BASE_DIR + "/data/login_data.json", encoding="utf-8") as f:
        data = json.load(f)
        data_list = list()
        for i in data.values():
            data_list.append((
                i.get("username"),
                i.get("password"),
                i.get("code"),
                i.get("expect"),
            ))

        logging.info(data_list)
        return data_list


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """类级别 Fixture 打开浏览器 初始化首页 和 登录页的 业务层对象"""
        cls.driver = DriverUtil.get_driver()
        cls.index_proxy = IndexProxy()
        cls.login_proxy = LoginProxy()

    @classmethod
    def tearDownClass(cls):
        """类级别 Fixture 关闭浏览器 """
        DriverUtil.quit_driver()

    def setUp(self):
        """方法级别 Fixture 预制条件  打开首页  点击登录"""
        self.driver.get("http://127.0.0.1")  # 打开首页
        self.index_proxy.go_to_login()  # 点击登录

    def tearDown(self):
        """方法级别 Fixture """
        time.sleep(2)  # 暂停2秒

    @parameterized.expand(read_json)
    def test_login(self, username, password, code, expect):
        self.login_proxy.login(username, password, code)  # 实现登录
        time.sleep(3)
        title = self.driver.title  # 获取title
        logging.info(title)

        # 断言 有异常 截图
        try:
            self.assertIn(expect, title)
        except AssertionError as e:
            exc_info = sys.exc_info()[1]
            logging.info(exc_info)
            file_name = time.strftime("%Y%m%d%H%M%S")
            self.driver.get_screenshot_as_file(f"../screenshot/bug_{file_name}.png")
            raise e
