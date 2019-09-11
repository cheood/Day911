"""
登录页
"""
from selenium.webdriver.common.by import By

from C_WebAutoTestTPshop.base.base_page import BaseHandle, BasePage


class LoginPage(BasePage):
    """登录页--对象库层"""

    def __init__(self):
        super().__init__()  # 继承父类

        # 初始化 定位元素的 类型 属性

        self.username = (By.ID, "username")  # 用户名
        self.password = (By.ID, "password")  # 密码
        self.verify_code = (By.ID, "verify_code")  # 验证码
        self.login_btn = (By.NAME, "sbtbutton")  # 验证码

    def find_username(self):
        """
        登录页--定位用户名
        :return:  用户名元素对象
        """
        return self.find_element_func(self.username)

    def find_password(self):
        """
        登录页--定位用户名
        :return:  用户名元素对象
        """
        return self.find_element_func(self.password)

    def find_verify_code(self):
        """
        登录页--定位用户名
        :return:  用户名元素对象
        """
        return self.find_element_func(self.verify_code)

    def find_login_btn(self):
        """
        登录页--定位用户名
        :return:  用户名元素对象
        """
        return self.find_element_func(self.login_btn)


class LoginHandle(BaseHandle):
    """登录页--操作层"""

    def __init__(self):
        """初始化 对象库层对象"""
        self.login_page = LoginPage()

    def input_username(self, username):
        """
        登录页--用户名输入方法
        :param username:用户名
        :return: None
        """
        self.input_text(self.login_page.find_username(), username)

    def input_password(self, password):
        """
        登录页--密码输入方法
        :param :密码
        :return: None
        """
        self.input_text(self.login_page.find_password(), password)

    def input_verify_code(self, code):
        """
        登录页--验证码输入方法
        :param : 验证码
        :return: None
        """
        self.input_text(self.login_page.find_verify_code(), code)

    def click_login_btn(self):
        """
        登录页--点击登录按钮
        :return: None
        """

        self.click_element(self.login_page.find_login_btn())


class LoginProxy(object):
    """登录页--业务层"""

    def __init__(self):
        """初始化操作层对象"""
        self.login_handle = LoginHandle()

    def login(self, username, password, code):
        """
        登录页--登录方法
        :param username: 用户名
        :param password: 密码
        :param code: 验证码
        :return: None
        """
        self.login_handle.input_username(username)  # 输入用户名
        self.login_handle.input_password(password)  # 输入密码
        self.login_handle.input_verify_code(code)  # 输入验证码
        self.login_handle.click_login_btn()  # 点击登录按钮
