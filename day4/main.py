import unittest
import os
from BeautifulReport.BeautifulReport import BeautifulReport
# 收集用例
cases_dir = os.path.dirname(os.path.abspath(__file__))
s = unittest.TestLoader().discover(cases_dir)

br = BeautifulReport(s)
br.report("py30测试报告", "report.html")
