

import os
# 所有项目的基础目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 测试用例路径
ceses_dir = os.path.join(base_dir, "Testcases")
# 测试数据路径
datas_dir = os.path.join(base_dir, "Testdatas")

# 测试报告
report_dir = os.path.join(base_dir, "Outputs/report")
# print(report_dir)
# 日志的路径
logs_dir = os.path.join(base_dir, "Outputs/log")
# 配置文件路径
conf_dir = os.path.join(base_dir, "Conf")
