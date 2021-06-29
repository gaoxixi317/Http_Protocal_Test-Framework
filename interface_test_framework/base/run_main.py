from interface_test_framework.util.get_data import GetData
from interface_test_framework.base.run_method import RunMethod
from interface_test_framework.util.operate_excel import OperateExcel
from interface_test_framework.config.data_config import GlobalConfig
from interface_test_framework.util.common import Common

class RunMain:

    def __init__(self):
        self.data = GetData()
        self.op_exl = OperateExcel()
    # def run_tests(self):
    #     row_count = self.data.get_case_lines()
    #     for i in range(1, row_count):
    #         if self.data.get_is_run(i+1):
    #             url = self.data.get_url(i+1)
    #             data = self.data.get_request_data(i+1)
    #             headers = self.data.get_header(i+1)
    #             method = self.data.get_request_method(i+1)
    #             if method == 'get':
    #                 result = RunMethod.get_main(url, data, headers)
    #             else:
    #                 result = RunMethod.post_main(url, data, headers)
    #             exp_result = self.data.get_exp_result(i+1)
    #             self.op_exl.write_result(i+1, GlobalConfig.get_value('act_result'), result.text)
    #             if exp_result in result.text:
    #                 self.op_exl.write_result(i+1, GlobalConfig.get_value('test_result'), '测试通过')
    #             else:
    #                 self.op_exl.write_result(i+1, GlobalConfig.get_value('test_result'), '测试失败')
    #             self.op_exl.write_result(i+1, GlobalConfig.get_value('exec_time'), Common.get_current_time())

    def run_tests(self):
        row_count = self.data.get_case_lines()
        for i in range(2, row_count+1):
            if self.data.get_is_run(i):
                url = self.data.get_url(i)
                data = self.data.get_request_data(i)
                headers = self.data.get_header(i)
                method = self.data.get_request_method(i)
                if method == 'get':
                    result = RunMethod.get_main(url, data, headers)
                else:
                    result = RunMethod.post_main(url, data, headers)
                exp_result = self.data.get_exp_result(i)
                self.op_exl.write_result(i, GlobalConfig.get_value('act_result'), result.text)
                if exp_result in result.text:
                    self.op_exl.write_result(i, GlobalConfig.get_value('test_result'), '测试通过')
                else:
                    self.op_exl.write_result(i, GlobalConfig.get_value('test_result'), '测试失败')
                self.op_exl.write_result(i, GlobalConfig.get_value('exec_time'), Common.get_current_time())

if __name__ == '__main__':
    rm = RunMain()
    rm.run_tests()