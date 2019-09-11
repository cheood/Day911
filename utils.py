"""
公共方法类
"""
import time
from selenium import webdriver


def switch_new_window():
    """切换新窗口d的方法"""
    driver = DriverUtil.get_driver()
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])


def find_element_for_text(text):
    """跟具文本内容  定位元素  有元素返回元素本身  没有元素返回 False"""
    ele_path = "//*[contains(text(),'{}')]".format(text)
    try:
        driver = DriverUtil.get_driver()
        element = driver.find_element_by_xpath(ele_path)
        return element
    except Exception:
        return False


class DriverUtil(object):
    """浏览器驱动工具类"""
    _driver = None  # 设置浏览器对象初始化状态 (保护变量)
    _driver_status = True  # 浏览器驱动开关

    @classmethod
    def get_driver(cls):
        """获取浏览器对象方法"""
        # 为了防止反复创建浏览器对象, 需要对浏览器对象是否存在进行判断
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.get('http://127.0.0.1')
            cls._driver.maximize_window()  # 窗口最大化
            cls._driver.implicitly_wait(10)  # 隐式等待
        return cls._driver

    @classmethod
    def quit_driver(cls):
        """退出浏览器对象方法"""
        # 需要判断浏览器对象存在, 才能执行退出操作, 否则会报错!
        # if self.driver is not None:
        if cls._driver and cls._driver_status:
            cls._driver.quit()
            cls._driver = None  # 此代码是确保浏览器对象会被从内存中移除掉

    @classmethod
    def change_driver_status(cls, status):
        """浏览器驱动开关 设置放法"""
        cls._driver_status = status


if __name__ == '__main__':
    DriverUtil.get_driver()
    time.sleep(3)
    DriverUtil.quit_driver()
