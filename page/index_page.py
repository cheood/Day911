"""
首页
"""
from selenium.webdriver.common.by import By

from C_WebAutoTestTPshop.base.base_page import BasePage, BaseHandle


class IndexPage(BasePage):
    """首页--对象库层"""

    def __init__(self):
        super().__init__()  # 继承父类

        # 初始化 定位元素的 类型 和 属性
        self.login_link = (By.LINK_TEXT, "登录")  # 首页上的登录元素
        self.search_bar = (By.ID, "q")  # 搜索框
        self.search_btn = (By.CLASS_NAME, "ecsc-search-button")  # 搜索按钮
        self.goods_cart_btn = (By.CSS_SELECTOR, ".share-shopcar-index")  # 购物无车元素
        self.my_order_link = (By.LINK_TEXT, "我的订单")  # 我的订单链接

    def find_login_link(self):
        """
        首页 -- 定位登录元素
        :return: 登录元素对象
        """
        return self.find_element_func(self.login_link)

    def find_search_bar(self):
        """首页--定位搜索框"""
        return self.find_element_func(self.search_bar)

    def find_search_btn(self):
        """首页--定位搜索按钮"""
        return self.find_element_func(self.search_btn)

    def find_goods_cart_btn(self):
        """首页--定位购物车按钮"""
        return self.find_element_func(self.goods_cart_btn)

    def find_my_order_link(self):
        """首页--定位我的订单链接"""
        return self.find_element_func(self.my_order_link)


class IndexHandle(BaseHandle):
    """首页--操作层"""

    def __init__(self):
        """初始化 对象库层 对象"""
        self.index_page = IndexPage()

    def click_login_link(self):
        """
        首页--点击登录元素
        :return: None
        """
        self.click_element(self.index_page.find_login_link())

    def input_search_bar(self, kw):
        """首页--给搜索框输入搜索内容"""
        self.input_text(self.index_page.find_search_bar(), kw)

    def click_search_btn(self):
        """首页--点击搜索按钮"""
        self.click_element(self.index_page.find_search_btn())

    def click_goods_cart_btn(self):
        """首页--点击购物车按钮"""
        self.click_element(self.index_page.find_goods_cart_btn())

    def click_my_order_link(self):
        """首页--我的订单连接"""
        self.click_element(self.index_page.find_my_order_link())


class IndexProxy(object):
    """首页--业务层"""

    def __init__(self):
        """初始化 操作层对象"""
        self.index_handle = IndexHandle()

    def go_to_login(self):
        """
        首页--去登录页面的方法
        :return: None
        """
        self.index_handle.click_login_link()

    def go_to_search_list(self, kw):
        """首页--去搜索列表页的放法"""
        self.index_handle.input_search_bar(kw)  # 输入搜索内容
        self.index_handle.click_search_btn()  # 点击搜索按钮

    def go_to_goods_card(self):
        """首页--去购物车法"""
        self.index_handle.click_goods_cart_btn()  # 点击购物车

    def go_to_my_order(self):
        """首页--去我的订单页面方法"""
        self.index_handle.click_my_order_link()
