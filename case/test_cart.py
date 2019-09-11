"""
测试 购物车
"""
import logging
import unittest

from C_WebAutoTestTPshop.page.goods_detail_page import GoodsDetailProxy
from C_WebAutoTestTPshop.page.index_page import IndexProxy
from C_WebAutoTestTPshop.page.search_list_page import GoodsListProxy
from C_WebAutoTestTPshop.utils import DriverUtil


class TestCart(unittest.TestCase):
    """测试用例  测试购物车添加的商品类"""

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()  # 初始化浏览器驱动对象

        cls.index_proxy = IndexProxy()  # 首页  业务对象
        cls.goods_list_proxy = GoodsListProxy()  # 搜索列表 业务对象
        cls.goods_detail_proxy = GoodsDetailProxy()  # 详情页  业务对象

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    def setUp(self):
        self.driver.get("http://127.0.0.1")

    def test_cat(self):
        """测试 加入购物车方法"""
        kw = "小米手机5"
        self.index_proxy.go_to_search_list(kw)  # 首页输入关键字 跳转到搜索列表页
        self.goods_list_proxy.go_to_goods_detail(kw)  # 点击商品 进入详情页
        self.goods_detail_proxy.add_cart()  # 点击加入购物车 获取提示弹窗
        result = self.goods_detail_proxy.get_add_cart_result_fun()
        logging.info(result)
        self.assertIn("添加成功", result)
