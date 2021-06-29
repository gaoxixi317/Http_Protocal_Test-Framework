from interface_test_framework.util.operate_excel import OperateExcel
from interface_test_framework.config.data_config import GlobalConfig
from interface_test_framework.util.common import Common
# 获取测试数据文件中的测试数据
class GetData:

    def __init__(self):
        self.op_excl = OperateExcel()

    def get_case_lines(self):
        return self.op_excl.get_lines()

    # 获取模板中url的值
    def get_url(self, row):
        col = GlobalConfig.get_value('url')
        return self.op_excl.get_value(row, col)

    # 获取是否运行列的值
    def get_is_run(self, row):
        col = GlobalConfig.get_value('is_run')
        flag = self.op_excl.get_value(row, col)
        if flag == 'yes':
            return True
        else:
            return False

    # 获取请求类型的值
    def get_request_method(self, row):
        col = GlobalConfig.get_value('request_method')
        return self.op_excl.get_value(row, col)

    # 获取headers的值
    def get_header(self, row):
        col = GlobalConfig.get_value('header')
        header = self.op_excl.get_value(row, col)
        if header == 'N/A':
            return None
        else:
            return header

    def get_request_data(self, row):
        col = GlobalConfig.get_value('request_data')
        request_data = self.op_excl.get_value(row, col)
        if request_data != 'N/A':
            # 根据get和post不同的请求格式构造对应的数据格式
            if self.get_request_method(row) == 'get':
                return Common.get_request_data_str(request_data)
            elif self.get_request_method(row) == 'post':
                return Common.get_request_data_dict(request_data)
        else:
            return None

    # 获取预期结果的值
    def get_exp_result(self, row):
        col = GlobalConfig.get_value('exp_result')
        return self.op_excl.get_value(row, col)