"""
我的账户页
"""
from selenium.webdriver.common.by import By

from C_WebAutoTestTPshop.base.base_page import BasePage, BaseHandle


class MyOrderPage(BasePage):
    """我的订单页--对象库层"""

    def __init__(self):
        super().__init__()

        # 初始化 定位元素的 类型 和 属性
        self.wait_for_pay = (By.LINK_TEXT, "待付款")
        self.now_pay = (By.LINK_TEXT, "立即支付")

    def find_wait_for_pay(self):
        """定位待付款的方法"""
        return self.find_element_func(self.wait_for_pay)

    def find_now_pay(self):
        """定位立即支付的方法"""
        return self.find_element_func(self.now_pay)


class MyOrderHandle(BaseHandle):
    """我的订单页--操作层"""

    def __init__(self):
        self.my_account_page = MyOrderPage()

    def click_wait_for_pay(self):
        """我的订单页--点击待支付方法"""
        self.click_element(self.my_account_page.find_wait_for_pay())

    def click_now_pay(self):
        """我的订单页--点击立即支付方法"""
        self.click_element(self.my_account_page.find_now_pay())


class MyOrderProxy(object):
    """我的订单页--业务层"""

    def __init__(self):
        self.my_account_handle = MyOrderHandle()

    def go_to_order_pay(self):
        """跳转到订单支付页面"""
        self.my_account_handle.click_wait_for_pay()  # 点击待付款
        self.my_account_handle.click_now_pay()  # 点击立即付款
