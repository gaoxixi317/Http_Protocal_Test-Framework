class GlobalConfig:

    @classmethod
    def get_value(cls, col):
        dic = {
            'id': 1
            ,'module': 2
            ,'url': 3
            ,'is_run': 4
            ,'request_method': 5
            ,'header': 6
            ,'request_data': 7
            ,'exp_result': 8
            ,'act_result': 9
            ,'test_result': 10
            ,'exec_time': 11
        }
        return dic[col]

if __name__ == '__main__':
    print(GlobalConfig.get_value('url'))