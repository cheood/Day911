"""
搜索列表页
"""
from selenium.webdriver.common.by import By

from C_WebAutoTestTPshop.base.base_page import BasePage, BaseHandle


class GoodsListPage(BasePage):
    """商品列表--对象库层"""

    def __init__(self):
        super().__init__()

        self.goods = (By.XPATH, "//*[@class='shop_name2']/*[contains(text(),'{}')]")  # 定位搜索到的商品

    def find_goods(self, kw):
        """定位搜索到的商品方法"""
        location = (self.goods[0], self.goods[1].format(kw))
        return self.find_element_func(location)


class GoodsListHandle(BaseHandle):
    """商品列表--操作层"""

    def __init__(self):
        self.goods_list_page = GoodsListPage()

    def click_goods(self, kw):
        """商品列表--点击搜索到的商品方法"""
        self.click_element(self.goods_list_page.find_goods(kw))


class GoodsListProxy(object):
    """商品列表--业务层"""

    def __init__(self):
        self.goods_list_handle = GoodsListHandle()

    def go_to_goods_detail(self, kw):
        """商品列表--跳转到商品详情页方法"""
        self.goods_list_handle.click_goods(kw)
