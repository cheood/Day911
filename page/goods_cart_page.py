"""
购物车页面
"""
from selenium.webdriver.common.by import By

from C_WebAutoTestTPshop.base.base_page import BasePage, BaseHandle


class GoodsCartPage(BasePage):
    """购物车--对象库层"""

    def __init__(self):
        super().__init__()

        self.check_all = (By.CLASS_NAME, "checkCartAll")  # 全选复选框
        self.go_check = (By.LINK_TEXT, "去结算")  # 去结算

    def find_check_all(self):
        """购物车--定位全选复选框方法"""
        return self.find_element_func(self.check_all)

    def find_go_check(self):
        """购物车--定位去结算按钮方法"""
        return self.find_element_func(self.go_check)


class GoodsCartHandle(BaseHandle):
    """购物车--操作层"""

    def __init__(self):
        self.goods_cart_page = GoodsCartPage()

    def click_check_all(self):
        """购物车--点击复选框"""
        ele_check_all = self.goods_cart_page.find_check_all()
        if not ele_check_all.is_selected():
            self.click_element(ele_check_all)

    def click_go_check(self):
        """购物车--点击去结算方法"""
        self.click_element(self.goods_cart_page.find_go_check())


class GoodsCartProxy(object):
    """购物车--业务层"""

    def __init__(self):
        self.goods_cart_handle = GoodsCartHandle()

    def go_to_order_check(self):
        self.goods_cart_handle.click_check_all()  # 点击全选
        self.goods_cart_handle.click_go_check()  # 点击去结算
