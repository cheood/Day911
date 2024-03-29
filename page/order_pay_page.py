"""
订单支付页面
"""

from selenium.webdriver.common.by import By

from C_WebAutoTestTPshop.base.base_page import BasePage, BaseHandle


class OrderPayPage(BasePage):
    """订单支付页--对象库层"""

    def __init__(self):
        super().__init__()

        # 初始化 定位元素的 类型 和 属性
        self.after_pay = (By.CSS_SELECTOR, "[value='pay_code=cod']")  # 货到付款
        self.confirm_pay = (By.LINK_TEXT, "确认支付方式")  # 确认支付方式

    def find_after_pay(self):
        """订单支付页--定位货到付款"""
        return self.find_element_func(self.after_pay)

    def find_confirm_pay(self):
        """订单支付页--定位确认支付方式"""
        return self.find_element_func(self.confirm_pay)


class OrderPayHandle(BaseHandle):
    """订单支付页--操作层"""

    def __init__(self):
        self.order_pay_page = OrderPayPage()

    def click_after_pay(self):
        """订单支付页--点击货到付款"""
        self.click_element(self.order_pay_page.find_after_pay())

    def click_confirm_pay(self):
        """订单支付页--点击确认支付方式"""
        self.click_element(self.order_pay_page.find_confirm_pay())


class OrderPayProxy(object):
    """订单支付页--业务层"""

    def __init__(self):
        self.order_pay_handle = OrderPayHandle()

    def order_pay_func(self):
        """订单支付页--订单支付方法"""
        self.order_pay_handle.click_after_pay()  # 点击货到付款
        self.order_pay_handle.click_confirm_pay()  # 点击确认支付方式
