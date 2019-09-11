"""
配置文件 在整个工程的最先执行文件中 调用config配置文件
"""
import logging.handlers
import os

# 获取当前文件所在的工程名的绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# 日志设置 方法
def config_log():
    """日志配置方法"""
    # 初始化日志器
    logger = logging.getLogger()
    # 修改日志输出级别
    logger.setLevel(level=logging.INFO)

    # 初始化处理器
    # 控制台
    sh = logging.StreamHandler()
    # 文件
    th = logging.handlers.TimedRotatingFileHandler(filename=BASE_DIR + '/log/info.log',
                                                   when='S',
                                                   interval=3,
                                                   backupCount=4)

    # 初始化格式器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt=fmt)

    # 添加格式器到处理器

    # sh.setFormatter(formatter)
    th.setFormatter(formatter)

    # 添加处理器到日志器
    logger.addHandler(sh)
    logger.addHandler(th)
