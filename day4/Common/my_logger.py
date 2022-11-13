import logging
import yaml
import os

from Python_Interface.A_2_Requests_register.Common.handle_config import conf
from Python_Interface.A_2_Requests_register.Common.handle_path import logs_dir


class Mylogger(logging.Logger):

    def __init__(self, file=None):
        # 设置输出级别、输出渠道、输出日志格式
        super().__init__(conf.get("log", "name"), conf.get("log", "level"))

        # 设置日志格式
        fml = "%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d行: %(message)s"
        formatter = logging.Formatter(fml)

        # 控制台渠道
        # 设置日志输出在哪些渠道
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        if file:
            # 文件渠道
            handle2 = logging.FileHandler(file, encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)


# 是否需要写入文件
if conf.getboolean("log", "file_ok"):
    file_name = os.path.join(logs_dir, conf.get("log", "file_name"))
else:
    file_name = None

logger = Mylogger(file_name)

logger.info("1111111111")









# logger = Mylogger("log", file="my_logger.log")
# if __name__ == '__main__':
#     logger = Mylogger("aaa")
#     logger.info("测试我自己封装的")
