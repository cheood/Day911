"""
组装测试用例
"""

import unittest
from C_WebAutoTestTPshop.case.test_cart import TestCart
from C_WebAutoTestTPshop.case.test_login import TestLogin
from C_WebAutoTestTPshop.case.test_order import TestOrder
from C_WebAutoTestTPshop.utils import DriverUtil

# 　套件
suite = unittest.TestSuite()

# 设置浏览器驱动开关  每个用例执行完毕不关闭浏览器
DriverUtil.change_driver_status(False)

# 组装
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestCart))
suite.addTest(unittest.makeSuite(TestOrder))

# 执行
unittest.TextTestRunner().run(suite)

# 执行完成后手动关闭浏览器驱动
DriverUtil.change_driver_status(True)
DriverUtil.quit_driver()
