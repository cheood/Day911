"""
订单--测试用例  不能单独执行  需要和登录用例  购物车用例 建立依赖  要放在测试套件中
订单支付--测试用例
"""
import logging
import time
import unittest

from C_WebAutoTestTPshop.page.goods_cart_page import GoodsCartProxy
from C_WebAutoTestTPshop.page.index_page import IndexProxy
from C_WebAutoTestTPshop.page.my_order_page import MyOrderProxy
from C_WebAutoTestTPshop.page.order_pay_page import OrderPayProxy
from C_WebAutoTestTPshop.page.oreder_check_page import OrderCheckProxy
from C_WebAutoTestTPshop.utils import DriverUtil, find_element_for_text, switch_new_window


class TestOrder(unittest.TestCase):
    """测试订单"""

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()

        # 初始化 依赖对象
        cls.index_proxy = IndexProxy()  # 首页业务对象
        cls.goods_cart_proxy = GoodsCartProxy()  # 购物车业务对象
        cls.order_check_proxy = OrderCheckProxy()  # 订单业务对象

        cls.my_order_proxy = MyOrderProxy()  # 我的订单业务对象
        cls.order_pay_proxy = OrderPayProxy()  # 订单支付业务对象

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    def setUp(self):
        self.driver.get("http://127.0.0.1")

    def test_order(self):
        """订单测试方法"""
        self.index_proxy.go_to_goods_card()  # 去购物车
        self.goods_cart_proxy.go_to_order_check()  # 去结算
        time.sleep(3)
        self.order_check_proxy.submit_order_func()  # 去提交订单

        time.sleep(5)
        result = find_element_for_text("订单提交成功")  # 返回订单提交成功 的 信息
        logging.info(result)
        # 断言
        self.assertTrue(result)

    def test_pay(self):
        """订单支付测试方法  订单测试执行后 执行  订单支付测试"""
        self.index_proxy.go_to_my_order()  # 首页点击我的订单

        # 切换新窗口
        switch_new_window()
        self.my_order_proxy.go_to_order_pay()  # 点击立即支付

        # 切换新窗口
        switch_new_window()

        self.order_pay_proxy.order_pay_func()  # 点击确认支付

        # 获取支付结果
        result = find_element_for_text("订单提交成功")
        logging.info(result)
        # 断言
        self.assertTrue(result)
