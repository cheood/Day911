"""
测试报告
"""
import time
import unittest

from C_WebAutoTestTPshop.case.test_cart import TestCart
from C_WebAutoTestTPshop.case.test_login import TestLogin
from C_WebAutoTestTPshop.case.test_order import TestOrder
from C_WebAutoTestTPshop.report.HTMLTestRunnerCN import HTMLTestReportCN

from C_WebAutoTestTPshop.utils import DriverUtil

# 设置开关 不让关闭浏览器
DriverUtil.change_driver_status(False)

# 套件
suite = unittest.TestSuite()
# 组装
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestCart))
suite.addTest(unittest.makeSuite(TestOrder))

# 执行
file_name = time.strftime("%Y%m%d%H%M%S")

with open(f"./tp_shop_report_{file_name}.html", "wb") as f:
    runner = HTMLTestReportCN(stream=f,
                              verbosity=2,
                              title="TPShop 测试报告",
                              description="系统 window  语言 python",
                              tester="程恒飞")
    runner.run(suite)

# 设置开关 并手动关闭
DriverUtil.change_driver_status(True)
DriverUtil.quit_driver()
