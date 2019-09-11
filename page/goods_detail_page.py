"""
商品详情页
"""
from selenium.webdriver.common.by import By

from C_WebAutoTestTPshop.base.base_page import BasePage, BaseHandle
from C_WebAutoTestTPshop.utils import DriverUtil


class GoodsDetailPage(BasePage):
    """商品详情页--对象库层"""

    def __init__(self):
        super().__init__()

        # 初始化 定位元素的 类型和属性
        self.add_cart_btn = (By.ID, "join_cart")  # 点击加入购物车
        self.add_cart_result = (By.CSS_SELECTOR, ".conect-title>span")  # 获取加入结果  此处取的是父类

    def find_add_cart_btn(self):
        """商品详情页--定位加入购物车按钮"""
        return self.find_element_func(self.add_cart_btn)

    def find_add_cart_result(self):
        """商品详情页--定位加入操作后的提示信息的元素"""
        return self.find_element_func(self.add_cart_result)


class GoodsDetailHandle(BaseHandle):
    """商品详情页--操作层"""

    def __init__(self):
        self.goods_detail_page = GoodsDetailPage()

    def click_add_cart_btn(self):
        """商品详情页--点击加入购物车按钮"""
        self.click_element(self.goods_detail_page.find_add_cart_btn())

    def get_add_cart_result(self):
        """商品详情页--返回加入后的提示信息"""
        # iframe
        driver = DriverUtil.get_driver()
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

        return self.get_element_text(self.goods_detail_page.find_add_cart_result())


class GoodsDetailProxy(object):
    """商品详情页--业务层"""

    def __init__(self):
        self.goods_detail_handle = GoodsDetailHandle()

    def add_cart(self):
        """商品详情页--加入购物车方法"""
        self.goods_detail_handle.click_add_cart_btn()  # 点击商品详情页上的加入购物车的按钮

    def get_add_cart_result_fun(self):
        """商品详情页--返回加入信息"""
        return self.goods_detail_handle.get_add_cart_result()  # 得到加入购物车后的返回信息


if __name__ == '__main__':
    pass
