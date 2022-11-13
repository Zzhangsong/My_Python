import unittest
from day4.Common.hadle_requests import send_requests
from day4.Common.handle_excel import HandleExcel
import os
from day4.Common.myddt import ddt, data
from day4.Common.handle_path import datas_dir

# file_path = os.path.join(datas_dir, +"/api_cases.xlsx", "注册")

he = HandleExcel(datas_dir+"/api_cases.xlsx", "注册")
cases = he.read_all_datas()
he.close_file()


@ddt
class TestRegister(unittest.TestCase):

    @data(*cases)
    def test_register_ok(self, case):
        # case = cases[0]
        expected = eval(case["expected"])
        resp = send_requests(case["method"], case["url"], case["request_data"])
        self.assertEqual(resp.json()["code"], expected["code"])
        self.assertEqual(resp.json()["msg"], expected["msg"])
